import json
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import karma
import airtable

app = App(token=os.getenv("HOUSES_SLACK_BOT_TOKEN"))


@app.event("message")
def _slack_message_listener(event, _say):
    karma_processor = karma.Karma(app)
    karma_detail = karma_processor.parse_karma_event(event)
    print(karma_detail)
    airtable.post(karma_detail)


def _main():
    handler = SocketModeHandler(app, os.getenv("HOUSES_SLACK_APP_TOKEN"))
    handler.start()


def _test():
    with open('example_event.json', 'r') as e:
        event = json.load(e)
        _slack_message_listener(event, None)


if __name__ == "__main__":
    _test()
