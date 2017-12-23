defmodule DittoApiWeb.Router do
  use DittoApiWeb, :router

  pipeline :ditto_api do
    plug :accepts, ["json"]
  end

  scope "/ditto_api", DittoApiWeb do
    pipe_through :ditto_api

    post "/slack/events", SlackController, :handle_slack_event
  end
end
