# 🎮 Game Shelf API

> **Projeto de exercício** desenvolvido como prática de estudo de FastAPI e MySQL, durante o 2º ano do curso técnico no **IFRN — Campus Caicó**.

API REST para gerenciar sua coleção pessoal de jogos. Organize seus jogos por status, plataforma e avaliação com operações CRUD completas.

---

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PyMySQL](https://pypi.org/project/PyMySQL/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- MySQL

---

## 📁 Estrutura do projeto

```
game-shelf-api/
├── main.py           # Inicialização da aplicação
├── database1.py      # Conexão com o banco de dados
├── models.py         # Modelo da tabela (SQLAlchemy)
├── schemas.py        # Schemas de entrada e saída (Pydantic)
├── .env              # Variáveis de ambiente (não versionado)
├── .gitignore
└── routers/
    └── games.py      # Rotas do CRUD
```

---

## 🔁 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/games/lista_jogos` | Lista todos os jogos |
| `GET` | `/games/buscar/{id}` | Busca um jogo pelo ID |
| `GET` | `/games/buscar_status/{status}` | Filtra jogos por status |
| `POST` | `/games/cadastrar_game` | Cadastra um novo jogo |
| `PUT` | `/games/atualizar_jogos/{id}` | Atualiza um jogo existente |
| `DELETE` | `/games/delete_games/{id}` | Remove um jogo |

---

## ▶️ Como rodar o projeto

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/game-shelf-api.git
cd game-shelf-api
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

**3. Instale as dependências**
```bash
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:
```
DATABASE_URL=mysql+pymysql://usuario:senha@localhost:3306/bd_games
```

**5. Crie o banco de dados no MySQL**
```sql
CREATE DATABASE bd_games;
```

**6. Suba o servidor**
```bash
uvicorn main:app --reload
```

**7. Acesse a documentação interativa**
```
http://localhost:8000/docs
```

---

## 📋 Status dos jogos disponíveis

- `PLAYING` — jogando atualmente
- `COMPLETED` — já zerou
- `WISHLIST` — quer jogar

---

## 👨‍💻 Autor

Desenvolvido por um aluno do **IFRN — Campus Caicó** como exercício de aprendizado de FastAPI com banco de dados relacional.
