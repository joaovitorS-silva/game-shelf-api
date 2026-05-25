from pydantic import BaseModel 
from typing import Optional

class GameSchema(BaseModel):
    title: str
    genre: str
    plataform: str
    status: str
    rating: int


class GameSchema_atulizar(BaseModel):
    title: Optional [str]
    genre: Optional [str]  
    plataform: Optional [str]
    status: Optional [str] = "WICHLIST"
    rating: Optional [int]

