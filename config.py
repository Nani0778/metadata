import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", '1101776571')) 
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "movieplaza77")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "movieplaza77")
CAPTION = os.environ.get("CAPTION", "")
DOWNLOAD_LOCATION = "./DOWNLOADS"
SUNRISES_PIC= "https://telegra.ph/file/1daf9d172ce29199dea44.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", ''))
