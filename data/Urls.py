import os
from dotenv import load_dotenv
load_dotenv()
STAGE = os.getenv("STAGE")

class Urls:

    HOST = f"https://{STAGE}-aqa.example.com"

    LOGIN_PAGE = f"{HOST}/login"
