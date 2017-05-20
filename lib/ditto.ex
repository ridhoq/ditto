defmodule Ditto do
  use Application

  def start(_type, _args) do
    import Supervisor.Spec, warn: false

    slack_token = Application.get_env(:ditto, :slack_token)
    redis_url = Application.get_env(:ditto, :redis_url)

    children = [
      worker(Redix, [redis_url, [name: :redix]]),
      worker(Slack.Bot, [Ditto.Bot, [], slack_token])
    ]

    opts = [strategy: :one_for_one, name: Ditto.Supervisor]
    {:ok, _pid} = Supervisor.start_link(children, opts)
  end
end

