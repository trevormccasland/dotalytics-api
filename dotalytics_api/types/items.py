from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    cost: int
    secret_shop: int
    side_shop: int
    recipe: int


class ItemsResult(BaseModel):
    items: List[Item]
    status: int


class GetGameItemsResponse(BaseModel):
    result: ItemsResult
