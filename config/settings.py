import os
import json


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "secrets.json")) as file:
    secrets = json.loads(file.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise Exception(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
ENV = get_secret("ENV")

# Server details
HOST = get_secret("HOST")
PORT = get_secret("PORT")
DEBUG = True if get_secret("DEBUG") == 'True' else False

# REDIS Search Settings
REDISSEARCH_URI = get_secret("REDISSEARCH_URI")
REDISSEARCH_INDEX = get_secret("REDISSEARCH_INDEX")
