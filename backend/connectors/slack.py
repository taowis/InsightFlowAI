class SlackClient:
    def __init__(self, bot_token: str): self.bot_token = bot_token
    def notify(self, channel: str, text: str):
        # TODO: Slack API chat.postMessage
        return {"ok": True}
