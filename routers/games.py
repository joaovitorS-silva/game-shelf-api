from fastapi import  Depends , HTTPException, APIRouter
from database1 import abrir_session , Session
from schemas import GameSchema
from models import Game_List

router_games = APIRouter(prefix="/games", tags=["/Game_Library "])

#listar todos jogos 
@router_games.get("/lista_jogos")
async def listar_todos_jogos(session: Session = Depends(abrir_session)):
    games = session.query(Game_List).all()

    return{
        "games": games,
        "teste": "testando jv"
    }
@router_games.get("/buscar/{id_busca}")
async def buscar_game(id_busca: int,session: Session = Depends(abrir_session)):
    busca = session.query(Game_List).filter(Game_List.id==id_busca).first()
    if not busca:
          raise HTTPException(status_code=402, detail="este jogo não possui na lista de jogos")
    else:
        return{
             "busca_feita": f"o jogo encontrado foi {busca.title}"
        }
    
@router_games.post("/cadastrar_game")
async def cadastrar_game(GameSchema: GameSchema ,   session: Session = Depends(abrir_session)):

    game_novo = Game_List(GameSchema.title, GameSchema.plataform,  GameSchema.status, GameSchema.rating,)

    session.add(game_novo)
    session.commit()
     
    return{
        "reposta": f"o {GameSchema.title}, foi adicionado com sucesso"
     }

        

