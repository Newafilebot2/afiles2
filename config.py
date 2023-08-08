




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6367599162:AAGpg6HWK8SpeOa5jMJMSF8V7jrVStdSNf0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25354498"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1cdcf1a33fc5108fa3ca151480eece50")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001952793463"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1969177696"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://od3brs9x:0oeTY8cRWnClU8os@cluster0.dihw6hm.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001224779387"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋 Hello {first}!\n\n Welcome to the File sender bot!🌟")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channels in order to use me\n\nKindly join both of them (Main and Private channel) </b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Hello there! \n\nPlease do not send me any direct message as I can only send you files once you click on any link.\n\nJoin @quality_ka_study_material for more 💦💦💦  "

ADMINS.append(OWNER_ID)
ADMINS.append(1969177696)


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
