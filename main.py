from typing import List
from fastapi import FastAPI
from models import Joke, JokeType

app = FastAPI()

db: List[Joke] = [
    Joke(
        setup="foo",
        punch_line="bar",
        joke_type=JokeType.groaner
    )
]


@app.get("/api/v1/jokes")
async def fetch_jokes():
    return db
