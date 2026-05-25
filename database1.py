from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker, Session
Base = declarative_base()

bd = create_engine("mysql+pymysql://root:1234@localhost:3306/bd_games")

def abrir_session():
    try:
        Session = sessionmaker(bind=bd)
        session = Session()
        yield session
    finally:
        session.close()






