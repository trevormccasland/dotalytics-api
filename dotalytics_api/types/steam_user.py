from pydantic import BaseModel
from typing import Optional


class ResolveVanityUrlItem(BaseModel):
    steamid: Optional[str]
    success: int
    message: Optional[str]


class ResolveVanityUrlResponse(BaseModel):
    response: ResolveVanityUrlItem
