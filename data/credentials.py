import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:

    STAGE = os.getenv("STAGE")

    if STAGE == "aqa":
        LOGIN = os.getenv("LOGIN")
        PASSWORD = os.getenv("PASSWORD")
    elif STAGE == "release":
        LOGIN = ""
        PASSWORD = ""



