from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.game_routes import game_api_router

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "Server is running..."


app.include_router(game_api_router)