import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    database_url: str = os.getenv("DATABASE_URL")
#   DATABASE_URL = os.getenv("DATABASE_URL")
#    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
#    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

settings = Settings()
