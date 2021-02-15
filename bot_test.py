from slack import WebClient
from bot_logic import Bot

SLACK_TOKEN = "xoxb-1746041751939-1742932769493-7fiEOv6jjuIF931PjnfvHCZd"

slac_web_client = WebClient(token=SLACK_TOKEN)

bot = Bot("#testworkspace")

message = bot.get_message_payload()

slac_web_client.chat_postMessage(**message)