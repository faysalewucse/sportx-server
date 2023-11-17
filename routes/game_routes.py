from fastapi import APIRouter
from config.database import collection
from models.game_model import Game
from schemas.game_schema import game_serializer, games_serializer

game_api_router = APIRouter()

# retreive


@game_api_router.get("/games")
async def get_games():
    games = games_serializer(collection.find())
    return games
