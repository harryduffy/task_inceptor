from slack_bolt import App
from flask import Flask, request, Response
from slack_bolt.adapter.flask import SlackRequestHandler
import requests
import json
from main import flask_app
# from main import flask_app
# from flask import Flask
# app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

app = App(
    token="xoxb-2338273112864-2353767630915-TDWUUknzvjKPubXMiuylrExC",
    signing_secret="153eaf8eb98394cf756945d8b251526d"
    )
handler = SlackRequestHandler(app)

@flask_app.route("/",methods=["POST", "GET","PUT"])
def challenge_response():
    print(request.json)
    if "challenge" in request.json:
        body = {"challenge": request.json['challenge']}

        return (json.dumps(body), 200, {"Content-Type":"application/json"})

@flask_app.route("/slack/events", methods=["POST", "GET","PUT"])
def slack_events():
    # handler runs App's dispatch method
    return handler.handle(request)

@app.command("/hello")
def message_hello( ack, say):
    # say() sends a message to the channel where the event was triggered
    ack()
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "Hey there !"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text="Hey there!"
    )

@app.action("button_click")
def action_button_click(body, ack, say,respond):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")
    respond({
    "delete_original": "true"
})

@app.event("message")
def handle_message_events(body, logger):
    pass


if __name__ == "__main__":
    flask_app.run(debug=True)