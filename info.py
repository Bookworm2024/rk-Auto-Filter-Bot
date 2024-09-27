import re, logging
from os import environ
from Script import script


def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f"Error - {type} is invalid, exiting now")
        exit()


def is_valid_ip(ip):
    ip_pattern = r"\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    return re.match(ip_pattern, ip) is not None


# Bot information
API_ID = environ.get("API_ID", "21145186")  # api id of your telegram id
if len(API_ID) == 0:
    print("Error - API_ID is missing, exiting now")
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")  # api hash of your telegram id
if len(API_HASH) == 0:
    print("Error - API_HASH is missing, exiting now")
    exit()
BOT_TOKEN = environ.get("BOT_TOKEN", "7296278954:AAHe8cUGdesQdvWRdBrWGXz_Z_SLBICGtVw")  # bot token from botfather
if len(BOT_TOKEN) == 0:
    print("Error - BOT_TOKEN is missing, exiting now")
    exit()
PORT = int(environ.get("PORT", "80"))  # don't change anything

# Bot pics
PICS = (
    environ.get(
        "PICS",
        "https://envs.sh/w75.jpg https://envs.sh/w7L.jpg https://envs.sh/wZg.jpg https://envs.sh/wZH.jpg https://envs.sh/w7c.jpg https://envs.sh/w7j.jpg https://envs.sh/w7Z.jpg",
    )
).split()

# Bot Admins
ADMINS = environ.get("ADMINS", "6011680723")  # apni tg id daalo
if len(ADMINS) == 0:
    print("Error - ADMINS is missing, exiting now")
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [
    int(index_channels) if index_channels.startswith("-") else index_channels
    for index_channels in environ.get("INDEX_CHANNELS", "-1002251367548 -1002317312223").split()
]
if len(INDEX_CHANNELS) == 0:
    print("Info - INDEX_CHANNELS is empty")
AUTH_CHANNEL = [
    int(auth_channels) for auth_channels in environ.get("AUTH_CHANNEL", "-1002398866124").split()
]
if len(AUTH_CHANNEL) == 0:
    print("Info - AUTH_CHANNEL is empty")
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002310300801")  # bot log channel -1005293546253
if len(LOG_CHANNEL) == 0:
    print("Error - LOG_CHANNEL is missing, exiting now")
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
IS_FSUB = is_enabled("IS_FSUB", True)

# support group
SUPPORT_GROUP = environ.get("SUPPORT_GROUP", "-1002249886020")  # support group id ex:  -1002936246860
if len(SUPPORT_GROUP) == 0:
    print("Error - SUPPORT_GROUP is missing, exiting now")
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://infohubstore06:k0nWe2dRtGZ9hq91@asphaltfive.egs31.mongodb.net/?retryWrites=true&w=majority&appName=asphaltfive")  # mongo db url
if len(DATABASE_URL) == 0:
    print("Error - DATABASE_URL is missing, exiting now")
    exit()
DATABASE_NAME = environ.get("DATABASE_NAME", "asphaltfive")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "Files")

# Links
SUPPORT_LINK = environ.get("SUPPORT_LINK", "https://t.me/Infohub_Tech")
UPDATES_LINK = environ.get("UPDATES_LINK", "https://t.me/infohub_updates")
FILMS_LINK = environ.get("FILMS_LINK", "https://t.me/movies_series_requestt")
TUTORIAL = environ.get("TUTORIAL", "https://t.me/infohub_updates")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/infohub_updates/34")

# Bot settings
DELETE_TIME = int(environ.get("DELETE_TIME", 600))  # Add time in seconds
CACHE_TIME = int(environ.get("CACHE_TIME", 300))
MAX_BTN = int(environ.get("MAX_BTN", 10))  # don't change anything in Language
LANGUAGES = [
    language.lower()
    for language in environ.get(
        "LANGUAGES", "english hindi telugu tamil kannada malayalam"
    ).split()
]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "hypershort.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "28cb820c966371de4aff06fc22d6a8a0bcf62b2c")
VERIFY_EXPIRE = int(environ.get("VERIFY_EXPIRE", 86400))  # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [
    extensions.lower()
    for extensions in environ.get("INDEX_EXTENSIONS", "mp4 mkv").split()
]
STICKERS_IDS = (
    "CAACAgIAAxkBAAJ4L2bpH96owEmpgDJ7N8o2kTvNfpzxAAKKOwACzURoSpOdH6cxMTITNgQ CAACAgIAAxkBAAJ1Zmbn_3GW3HJnOEDmvbWte8hbdMnRAAJpHQAC6SOISfMQhoEsm0L_NgQ CAACAgIAAxkBAAJ1Y2bn_2ernCrpa3qHXpLKvcuWrqM9AAKiGwACI6WQSYf-cz7ZdSttNgQ CAACAgIAAxkBAAJ1YGbn_0DtATuwgGb1qSGhnkqDFOErAALLGQACSTqQSd8HMPXDlDTnNgQ CAACAgIAAxkBAAJ1XWbn_wqbeJhJ4MVJCgIEsj47gAHaAAJMSAACYOdhSYFfH75aYcq_NgQ"
).split()

# boolean settings
GROUP_FSUB = is_enabled("GROUP_FSUB", False)
PM_SEARCH = is_enabled("PM_SEARCH", False)  # switch True or False for searching results in bot pm😃
IS_VERIFY = is_enabled("IS_VERIFY", False)
AUTO_DELETE = is_enabled("AUTO_DELETE", True)
WELCOME = is_enabled("WELCOME", False)
PROTECT_CONTENT = is_enabled("PROTECT_CONTENT", False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled("AUTO_FILTER", True)
IMDB = is_enabled("IMDB", True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled("SHORTLINK", False)


PAYMENT_QR = environ.get(
    "PAYMENT_QR", "https://envs.sh/wLE.jpg"
)  # telegraph link of your QR code
UPI_ID = environ.get("UPI_ID", "rajsom8877@okaxis")  # Add your upi id here
# for stream
IS_STREAM = is_enabled(
    "IS_STREAM", True
)  # true if you want stream feature active in your bot
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002465123057")  # if is_stream = true then add a channel id ex: -10026393639
if len(BIN_CHANNEL) == 0:
    print("Error - BIN_CHANNEL is missing, exiting now")
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "")  # if heroku then paste the app link here ex: https://heroku......./
if len(URL) == 0:
    print("Error - URL is missing, exiting now")
    exit()
else:
    if URL.startswith(("https://", "http://")):
        if not URL.endswith("/"):
            URL += "/"
    elif is_valid_ip(URL):
        URL = f"http://{URL}/"
    else:
        print("Error - URL is not valid, exiting now")
        exit()

