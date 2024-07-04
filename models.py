from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel


class JokeType(str, Enum):
    general = "general"
    knock_knock = "knock-knock"
    programming = "programming"
    dad = "dad"


class Joke(BaseModel):
    id: UUID = uuid4()
    type: str
    setup: str
    punchline: str
