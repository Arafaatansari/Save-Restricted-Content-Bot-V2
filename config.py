# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20117210"))
API_HASH = getenv("API_HASH", "f3157f5219adb380d6166b5c8ea8f8ec")
BOT_TOKEN = getenv("BOT_TOKEN", "8137507419:AAHYX3ATBRq30RKGa-kjMVbb7wPUVs3nhZc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8185737453").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://luffybot:qazmlpplm123@cluster0.yhz7t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-4703805137")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002468266807"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
