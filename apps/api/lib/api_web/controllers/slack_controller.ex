defmodule ApiWeb.SlackController do
    use ApiWeb, :controller

    def handle_slack_event(conn, params) do
        # handle url verification challenge
        if params["type"] == "url_verification" do
            conn 
            |> put_resp_content_type("application/json")
            |> send_resp(200, Poison.encode!(%{challenge: params["challenge"]}))
        end
    end
end