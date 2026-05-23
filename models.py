from sqlalchemy import String, Integer , Column
from database1 import Base

class Game_List(Base):
    __tablename__ = "game_vault"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String(255))
    genre = Column ("genre", String(60))
    plataform = Column ("plataform", String(60))
    status = Column ("status", String(60), default='WISHLIST')
    rating = Column ("rating", Integer)


    def __init__(self, title, genre, plataform, rating, status="WISHLIST"):
        self.title = title 
        self.genre = genre
        self.plataform = plataform
        self.rating = rating
        self.status = status
        

        




            #async def lista_games(id, title, genero, plataform, status, rating):