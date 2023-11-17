from fastapi import FastAPI
from routes.game_routes import game_api_router

app = FastAPI()


@app.get("/")
def root():
    return "Server is running..."


app.include_router(game_api_router)