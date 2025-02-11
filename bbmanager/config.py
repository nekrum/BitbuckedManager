import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Config:
    BB_ACCES_TOKEN = os.getenv("BB_ACCESS_TOKEN")
    BB_BASE_URL = os.getenv("BB_BASE_URL")
    BB_WORKSPACE_NAME = os.getenv("BB_WORKSPACE_NAME")
    BB_API_KEY = os.getenv("BB_API_KEY")
    BB_API_SECRET = os.getenv("BB_API_SECRET")
    BB_REFRESH_TOKEN = os.getenv("BB_REFRESH_TOKEN")
