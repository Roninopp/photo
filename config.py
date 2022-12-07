from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("7217645"))
API_HASH = getenv("78ba6352dd5cdc166fdef5aa84ba7c67")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("2100096282:AAEls5EFlORYva-cCFiXQ_xQZW2wbXIR2Wo")

# API By TechZBots || https://t.me/TechZBots
WALL_API = "https://techzbotsapi.herokuapp.com/wall?query="

UNSPLASH_API = "https://techzbotsapi.herokuapp.com/unsplash?query="

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://techz:wall@techzwallbotdb.katsq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
