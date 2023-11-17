from pymongo import MongoClient

mongodb_url = 'mongodb+srv://faysalewucse:DotDoWsIcZLSR4Q8@sportx.kehzdkr.mongodb.net/sportx'

# MongoDB Connection
client = MongoClient(mongodb_url)
database = client.sportx
collection = database["games"]
