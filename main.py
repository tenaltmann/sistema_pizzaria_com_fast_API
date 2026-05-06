from fastapi import FastAPI


app = FastAPI()

# SEMPRE Importar rotas após o "app = FastAPI()" para evitar erro de "referência circular"  

from auth_routes import auth_router     # mudar para routeR não repetir mesmo nome 
from order_routes import order_router   # mudar para routeR não repetir mesmo nome



app.include_router(auth_router)    # incluindo rotas de autenticação no app
app.include_router(order_router)   # incluindo rotas de pedidos no app

# para rodar o código, executar no terminal: uvicorn main:app --reload

# endpoints:
    # /ordens
    # /....


# Rest APIs
    # GET => Leitura/coleta
    # POST => enviar/criar
    # PUT / PATCH => edição
    # DELETE => deletar
    