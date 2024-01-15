from dotenv import load_dotenv
import os


# отримання з .env
load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
