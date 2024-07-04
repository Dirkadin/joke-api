from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
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
def fetch_jokes():
    return db


@app.post("/api/v1/jokes")
def new_joke(joke: Joke):
    db.append(joke)
    return {"id": joke.id}


@app.delete("/app/v1/jokes/{id}")
def delete_joke(id: UUID):
    for joke in db:
        if joke.id == id:
            db.remove(joke)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {id} does not exist"
    )
