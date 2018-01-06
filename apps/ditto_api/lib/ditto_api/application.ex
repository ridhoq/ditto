defmodule DittoApi.Application do
  use Application
  alias DittoKafka.Broker, as: Broker

  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  def start(_type, _args) do
    import Supervisor.Spec

    # set kafka_ex brokers on application start
    Application.put_env(:kafka_ex, :brokers, Broker.get_brokers())

    # Define workers and child supervisors to be supervised
    children = [
      # Start the endpoint when the application starts
      supervisor(DittoApiWeb.Endpoint, []),
      # Start your own worker by calling: DittoApi.Worker.start_link(arg1, arg2, arg3)
      # worker(DittoApi.Worker, [arg1, arg2, arg3]),
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: DittoApi.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  def config_change(changed, _new, removed) do
    DittoApiWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
