defmodule ApiWeb.SlackControllerTest do
    use ApiWeb.ConnCase

    test "handle_slack_event/2 responds to a challenge", %{conn: conn} do
        challenge_str = "issa_challenge"
        body = %{
            token: "issa_token",
            challenge: challenge_str,
            type: "url_verification"
        }

        response = conn
        |> post(slack_path(conn, :handle_slack_event), body)
        |> json_response(200)

        inspect(body)
        
        expected = %{"challenge" => challenge_str}

        assert response == expected
    end
end