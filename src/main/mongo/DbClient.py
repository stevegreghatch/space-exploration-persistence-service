import os
import logging
from pymongo import MongoClient
from dotenv import dotenv_values

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)


def load_env():
    if 'KUBERNETES_SERVICE_HOST' not in os.environ:
        env_vars = dotenv_values(".env")
        os.environ.update(env_vars)


load_env()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")

MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}.{MONGO_HOST}"

try:
    client = MongoClient(MONGO_URI)
    db = client["space_exploration"]
    logger.info('Connected successfully to MongoDB!')
except Exception as e:
    logger.info(f'Error connecting to MongoDB: {str(e)}')
