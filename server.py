import os
import logging
from pprint import pprint as pp

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from bot_logic import Bot

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_EVENTS_TOKEN = os.environ.get('SLACK_EVENTS_TOKEN')

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter(SLACK_EVENTS_TOKEN, "/api/msg", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


def bot_msg(channel, timestamp):
    """
    функция создает сообщение в класссе бота и отправляет его в слак
    """
    bot = Bot(channel)

    message = bot.get_message_payload()

    slack_web_client.chat_postMessage(**message)

    slack_web_client.reactions_add(channel=channel,
                                   name="thumbsup",
                                   timestamp=timestamp)


@slack_events_adapter.on("message")
def pars_message(payload):
    """
    фнукция парсит получаемые из чата сообщения
    """
    event = payload.get("event", {})
    pp(event)
    text = event.get("text")

    if "привет" in text.lower():
        channel_id = event.get("channel")
        msg_time = event.get("ts")

        return bot_msg(channel_id, msg_time)


if __name__ == "__main__":
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    logger.addHandler(logging.StreamHandler())
    app.run(host='0.0.0.0', port=8080)
