from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = "DocMind AI"
    VERSION = "0.1.0"
    DEBUG = True

settings = Settings()