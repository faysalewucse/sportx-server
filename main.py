from fastapi import FastAPI
from routes.game_routes import game_api_router

app = FastAPI()

app.include_router(game_api_router)