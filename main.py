from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

SECRET_KEY = str(os.getenv("SECRET_KEY"))  # Obtém a chave secreta do ambiente
ALGORITHM = str(os.getenv("ALGORITHM"))  # Obtém o algoritmo de criptografia do ambiente
ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))  # Obtém o tempo de expiração do token do ambiente, O 30 é o valor padrão caso a variável de ambiente não esteja definida



app = FastAPI()
# SEMPRE Importar rotas após o "app = FastAPI()" para evitar erro de "referência circular"  

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Configurando o contexto de criptografia para senhas
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login") # Configurando o esquema de autenticação OAuth2, definindo a URL para obtenção do token de acesso (neste caso, "auth/login")


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
    