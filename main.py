import json
import random
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Joke

app = FastAPI()

db: List[Joke] = []

d = json.load(open("jokes.json"))
for joke_json in d:
    joke = Joke.model_validate(joke_json)
    joke.id = uuid4()
    db.append(joke)


@app.get("/api/v1/jokes")
def fetch_jokes():
    return db


@app.get("/api/v1/jokes/random")
def random_joke():
    random_number = random.randrange(0, len(db) - 1, 1)
    return db[random_number]


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
