from fastapi import  Depends , HTTPException, APIRouter
from database1 import abrir_session , Session
from schemas import GameSchema , GameSchema_atulizar
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
             "busca_feita": f"o jogo encontrado foi ({busca.title})"
        }
    
@router_games.post("/cadastrar_game")
async def cadastrar_game(GameSchema: GameSchema ,   session: Session = Depends(abrir_session)):

    game_novo = Game_List(GameSchema.title,GameSchema.genre, GameSchema.plataform,  GameSchema.status, GameSchema.rating,)

    session.add(game_novo)
    session.commit()
     
    return{
        "reposta": f"o {GameSchema.title}, foi adicionado com sucesso"
     }

        
@router_games.put("/atualizar_jogos/{id_game}")
async def atulizar_jogos(id_game: int, GameSchema_atulizar: GameSchema_atulizar ,session: Session = Depends(abrir_session)):
    busca = session.query(Game_List).filter(Game_List.id==id_game).first()

    if not busca:
        raise HTTPException(status_code=402, detail="não existe esse jogo")
    else:
        busca.title = GameSchema_atulizar.title
        busca.genre = GameSchema_atulizar.genre
        busca.plataform = GameSchema_atulizar.plataform
        busca.status = GameSchema_atulizar.status
        busca.rating = GameSchema_atulizar.rating

    session.commit()
    session.refresh(busca)
    
    return{
        "mensagem": f"jogo com id: ({busca.id}) atualizado com sucesso",
        "atualização": (busca.rating, busca.status)
    }

@router_games.delete("/delete_games/{id_do_delete}")
async def deletar_games( id_do_delete:  int , session: Session = Depends(abrir_session)):
    busca = session.query(Game_List).filter(Game_List.id== id_do_delete).first()
    if not busca:
        raise HTTPException(status_code=401, detail=f"o id de numero ({id_do_delete}) nao existe")
    else:

        session.delete(busca)
        session.commit()
    return{
        "mensagem": f"jogo de id ({id_do_delete}) foi deletado"
    }        

@router_games.get("/buscar_status/{status_busca}")
async def buscar_status( status_busca: str  , session: Session = Depends(abrir_session)):
    busca = session.uqery(Game_List).filter(Game_List.status==status_busca).first()
    if busca:
        return{
            "mensagem": busca
        }
    else:
        raise HTTPException(status_code=401, detail="PROCURE POR , (playing), (complete), (WISHLIST)")