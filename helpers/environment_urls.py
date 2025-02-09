import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"
USERS_URL = f"{BASE_URL}/users?page=2"
BASE_URL_WITH_ENV = os.getenv("BASE_URL_VALUE")
USERS_URL_WITH_ENV = f"{BASE_URL_WITH_ENV}/users?page=2"