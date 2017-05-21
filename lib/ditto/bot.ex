defmodule Ditto.Bot do
  use Slack

  def handle_event(_message= %{type: "message", subtype: _}, _slack, state), do: {:ok, state}
  def handle_event(message = %{type: "message"}, slack, state) do
    if length(state) == 0 do
      state = set_state()
    end

    split_msg = String.split(message.text, " ")
    first_word = hd(split_msg)
    if (first_word == at(slack.me.id) or String.downcase(first_word) == slack.me.name) do
      command_with_args = tl(split_msg)
      command = hd(command_with_args) |> String.downcase
      args = tl(command_with_args)
      state =
        case command do
          "disable" ->
            handle_disable(message, slack, state)
          "enable" ->
            handle_enable(message, slack, state)
          "help" ->
            handle_help(message, slack, state)
          "ping" ->
            handle_ping(message, slack, state)
          "transform" ->
            handle_transform(args, message, slack, state)
          _ ->
            IO.puts "invalid command: #{command}"
        end
    else
      [lex_enabled | _tail] = state
      if Enum.member?(lex_enabled, message.user) do
        handle_lex_add(message, slack)
      end
    end

    {:ok, state}
  end
  def handle_event(_, _, state), do: {:ok, state}

  def set_state() do
    {:ok, retval} = Redix.command(:redix, ["SMEMBERS", "lex-enabled"])
    [retval]
  end

  def handle_disable(message, slack, state) do
    [lex_enabled | tail] = state
    if Enum.member?(lex_enabled, message.user) do
      {:ok, _retval} = Redix.command(:redix, ["SREM", "lex-enabled", message.user])
      lex_enabled = List.delete(lex_enabled, message.user)
      text = "#{at(message.user)}: your user is now disabled for transform"
      send_message(text, message.channel, slack)
      [lex_enabled | tail]
    else
      text = "#{at(message.user)}: your user is already disabled for transform"
      send_message(text, message.channel, slack)
      [lex_enabled | tail]
    end
  end

  def handle_help(message, slack, state) do
    text = """
    ditto disable - Disable transform for your user
    ditto help - Show this help message
    ditto enable - Enable transform for your user
    ditto transform <user> - Transform into user with a message
    ditto transform <user> <length> - Transform into user with a message of given length
    """
    send_message(text, message.channel, slack)
    state
  end

  def handle_enable(message, slack, state) do
    [lex_enabled | tail] = state
    if Enum.member?(lex_enabled, message.user) do
      text = "#{at(message.user)}: your user is already enabled for transform"
      send_message(text, message.channel, slack)
      [lex_enabled | tail]
    else
      {:ok, _retval} = Redix.command(:redix, ["SADD", "lex-enabled", message.user])
      lex_enabled = [message.user | lex_enabled]
      text = "#{at(message.user)}: your user is now enabled for transform"
      send_message(text, message.channel, slack)
      [lex_enabled | tail]
    end
  end

  def handle_ping(message, slack, state) do
    send_message("PONG", message.channel, slack)
    state
  end

  def handle_transform(args, message, slack, state) do
    {user_id, len} =
      case args do
        [user] ->
          {get_user_id(user, slack), 25}
        [user, len] ->
          {get_user_id(user, slack), String.to_integer(len)}
        _ -> {nil, nil}
      end
    if Enum.member?(hd(state), user_id) do
      lex_key = "lex:" <> user_id
      {:ok, lex} = Redix.command(:redix, ["LRANGE", lex_key, "0", "-1"])
      {:ok, chain} = Faust.generate_chain(Enum.join(lex, " "), 2)
      {:ok, text} = Faust.traverse(chain, len)
      IO.inspect text
      send_message(text, message.channel, slack)
    else
      text = "#{at(message.user)}: user not enabled for transform or not found"
      send_message(text, message.channel, slack)
    end
    state
  end

  def get_user_id(user, slack) do
    matches = Regex.scan(~r/<@(\S+?)>/, user)
    user_id =
      case length(matches) do
        n when n > 0 ->
          matches |> List.flatten |> tl |> hd
        _ -> lookup_user_id("@" <> user, slack)
      end
    user_id
  end

  def handle_lex_add(message, slack) do
    lex_key = "lex:" <> message.user
    {:ok, _retval} = Redix.command(:redix, ["RPUSH", lex_key, message.text])
    IO.puts("#{lookup_user_name(message.user, slack)} (#{message.user}) added to lex: #{message.text}")
  end

  def at(user_id), do: "<@#{user_id}>"

  def typeof(self) do
      cond do
          is_float(self)    -> "float"
          is_number(self)   -> "number"
          is_atom(self)     -> "atom"
          is_boolean(self)  -> "boolean"
          is_binary(self)   -> "binary"
          is_function(self) -> "function"
          is_list(self)     -> "list"
          is_tuple(self)    -> "tuple"
          true              -> "idunno"
      end
  end


end
