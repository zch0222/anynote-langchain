from dotenv import load_dotenv
import os

load_dotenv()

ORIGINS = os.environ.get("ORIGINS").split(",")
INDEX_PATH = os.environ.get("INDEX_PATH")
