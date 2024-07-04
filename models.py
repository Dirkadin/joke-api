from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel


class JokeType(str, Enum):
    joke = "joke"
    groaner = "groaner"
    dad_joke = "dad joke"


class Joke(BaseModel):
    id: UUID = uuid4()
    setup: str
    punch_line: str
    joke_type: JokeType
