import os

from flask import Flask
from slack import WebClient
import os
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events")
slack_web_client = WebClient(token=os.environ.get("SLACKBOT_TOKEN"))

MESSAGE_BLOCK = {
    "type": "seciton",
    "text": {
        "type": "mrkdwn",
        "text": ""
    }
}

@slack_events_adapter.on("message")
def message(payload):

    event = payload.get("event", {})

    text = event.get("text")

    if_"flip a coin" in text.lower():


if __name__ == '__main__':
    app.run()
