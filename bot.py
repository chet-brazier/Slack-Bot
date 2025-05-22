from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
INCIDENT_CHANNEL_ID = os.getenv("INCIDENT_CHANNEL_ID")

# Keywords to look for
KEYWORDS = ["true positive", "dispatched"]

# reminder text
REMINDER_TEXT = "For True Positives, please be sure to follow the checklist on Monday!"

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)

# Handle messages
@app.event("message")
def handle_message(event, client, logger):
    print("Message event received!")
    text = event.get("text", "").lower()
    user = event.get("user")
    channel = event.get("channel")

    if user and channel == INCIDENT_CHANNEL_ID and any(keyword in text for keyword in KEYWORDS):
        try:
            client.chat_postEphemeral(
                channel=channel,
                user=user,
                text=REMINDER_TEXT
            )
        except Exception as e:
            logger.error(f"Failed to send ephemeral message: {e}")

# Start the bot using Socket Mode
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
