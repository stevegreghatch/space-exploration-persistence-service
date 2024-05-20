from dotenv import dotenv_values
from pymongo import MongoClient

env_vars = dotenv_values(".env")

MONGO_USERNAME = env_vars.get("MONGO_USERNAME")
MONGO_PASSWORD = env_vars.get("MONGO_PASSWORD")
MONGO_HOST = env_vars.get("MONGO_HOST")
MONGO_URI = "mongodb+srv://{}:{}.{}".format(MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST)

client = MongoClient(MONGO_URI)
db = client["space_exploration"]
