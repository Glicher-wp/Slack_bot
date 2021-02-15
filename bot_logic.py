class Bot():
    """
    Базовый класс бота для осуществления взаимодействия с чатом
    """
    #базовая полезная нагрузка
    INTERMEDIA_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Let's Rock Here... \n\n"
            ),
        },
    }

    def __init__(self, channel):
        self.channel = channel

    def write_some_text(self):
        """
        метод генерирует текст сообщения в нужном формате
        """
        text = "Hellow World!"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}}

    def get_message_payload(self):
        """
        метод передает сгенерированный текст в чат
        """
        return {
            "channel": self.channel,
            "blocks": [
                self.INTERMEDIA_BLOCK,
                self.write_some_text(),
            ],
        }
