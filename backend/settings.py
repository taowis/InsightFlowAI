from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    env: str = os.getenv("ENV", "dev")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///clientpulse.db")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    google_project_id: str | None = os.getenv("GOOGLE_PROJECT_ID")
    google_client_email: str | None = os.getenv("GOOGLE_CLIENT_EMAIL")
    google_private_key: str | None = os.getenv("GOOGLE_PRIVATE_KEY")
    hubspot_token: str | None = os.getenv("HUBSPOT_TOKEN")
    slack_bot_token: str | None = os.getenv("SLACK_BOT_TOKEN")

settings = Settings()
