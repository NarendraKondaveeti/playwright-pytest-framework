import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    BASE_URL = os.getenv("BASE_URL")
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
    SLOW_MO = int(os.getenv("SLOW_MO", "500"))