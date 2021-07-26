import os
from dotenv import load_dotenv

load_dotenv('../.env')

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")