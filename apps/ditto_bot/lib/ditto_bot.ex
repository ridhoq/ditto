defmodule DittoBot do
  use Application

  def start(_type, _args) do
    import Supervisor.Spec, warn: false

    slack_token = Application.get_env(:ditto_bot, :slack_token)
    redis_url = Application.get_env(:ditto_bot, :redis_url)

    children = [
      worker(Redix, [redis_url, [name: :redix]]),
      worker(Slack.DittoBot, [DittoBot.Handler, [], slack_token])
    ]

    opts = [strategy: :one_for_one, name: DittoBot.Supervisor]
    {:ok, _pid} = Supervisor.start_link(children, opts)
  end
end

