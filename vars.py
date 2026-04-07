

from os import environ

API_ID = int(environ.get("API_ID", "22579742"))
API_HASH = environ.get("API_HASH", "2817067278f743a7f57e4dbea3e0d031")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "cricketlinksipl")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/cricketlinksipl")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "1380815395").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "1380815395"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





