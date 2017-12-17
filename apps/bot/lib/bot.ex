defmodule Bot do
  use Application

  def start(_type, _args) do
    import Supervisor.Spec, warn: false

    slack_token = Application.get_env(:bot, :slack_token)
    redis_url = Application.get_env(:bot, :redis_url)

    children = [
      worker(Redix, [redis_url, [name: :redix]]),
      worker(Slack.Bot, [Bot.Handler, [], slack_token])
    ]

    opts = [strategy: :one_for_one, name: Bot.Supervisor]
    {:ok, _pid} = Supervisor.start_link(children, opts)
  end
end

