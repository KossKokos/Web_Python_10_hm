
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://goitlearn:gNzmAJhyAtceMXpV@cluster.pdfljge.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)
db = client.homework_08
