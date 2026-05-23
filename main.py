from database1 import Base, bd
import models
Base.metadata.create_all(bd)
from fastapi import FastAPI 
from routers.games import router_games 

app = FastAPI()

app.include_router(router_games)

