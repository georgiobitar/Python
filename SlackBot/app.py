import os

from flask import Flask
from slack import WebClient
import os

app = Flask(__name__)

slack_web_client = WebClient(token=os.environ.get("SLACKBOT_TOKEN"))

@app.route('/')
def hello_world():
    return 'hello test'
if __name__ == '__main__':
    app.run()
