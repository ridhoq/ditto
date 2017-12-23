# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.
use Mix.Config

# General application configuration
config :ditto_api,
  namespace: DittoApi

# Configures the endpoint
config :ditto_api, DittoApiWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "VsvU/82G5LQqfGXRibnntxaY0xdL03oiSbkJHBWd4q0THLO72PXWeQ2hIsk4xFAv",
  render_errors: [view: DittoApiWeb.ErrorView, accepts: ~w(json)],
  pubsub: [name: DittoApi.PubSub,
           adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env}.exs"
