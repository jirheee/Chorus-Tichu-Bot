import os
from dotenv import load_dotenv

print(f".env Load Success? {load_dotenv('./.env')}")

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")