from typing import List

from pydantic import BaseModel


class Hero(BaseModel):
    name: str
    id: int


class HeroesResult(BaseModel):
    heroes: List[Hero]
    status: int
    count: int


class GetHeroesResponse(BaseModel):
    result: HeroesResult
