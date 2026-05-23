from pydantic import BaseModel

class GameSchema(BaseModel):
    title: str
    genre: str
    plataform: str
    status: str
    rating: int