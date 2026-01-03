import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "8312593787").split()))

API_ID = int(os.getenv("API_ID", "279666675544"))

API_HASH = os.getenv("API_HASH", "33947cf43d15de2796666755440ca0a8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8409555182:AAHhJzN2xxN6u6hRC2p6yiQd_uy4lEYgkgw")

OWNER_ID = int(os.getenv("OWNER_ID", "8312593787"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002886184276").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://uwa65721_db_user:IIj92rFd72o3Pr8W@cluster0.a2qzb2i.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-5246638707"))
