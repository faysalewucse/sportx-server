from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_games_data

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "Server is Running..."


@app.get("/games")
async def read_games():
    response = await fetch_games_data()
    return response
