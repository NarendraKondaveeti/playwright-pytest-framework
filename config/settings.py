import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("BASE_URL =", os.getenv("BASE_URL"))
print("BROWSER  =", os.getenv("BROWSER"))
print("HEADLESS =", os.getenv("HEADLESS"))
print("=" * 50)

class Settings:
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    BASE_URL = os.getenv("BASE_URL")
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
    SLOW_MO = int(os.getenv("SLOW_MO", "500"))