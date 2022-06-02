import pymongo
from dotenv.main import load_dotenv
import os


def connect():
    load_dotenv()
    connection_string = os.environ['connection_string']
    client = pymongo.MongoClient(connection_string)
    return client
