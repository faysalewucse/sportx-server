from motor.motor_asyncio import AsyncIOMotorClient
from models.game import GameData

url = 'mongodb+srv://faysalewucse:DotDoWsIcZLSR4Q8@sportx.kehzdkr.mongodb.net/sportx'

# MongoDB Connection
client = AsyncIOMotorClient(url)
database = client.sportx
collection = database.games

async def fetch_games_data():
    games = []
    cursor = collection.find({})
    async for document in cursor:
        game = GameData(**document)
        games.append(game)
    return games
