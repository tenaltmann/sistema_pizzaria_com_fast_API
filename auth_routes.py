from fastapi import APIRouter       # importando roteador
from models import Usuario      # importando modelo de usuario para criar conta
from sqlalchemy.orm import sessionmaker # importando sessionmaker para criar sessão de banco de dados

auth_router = APIRouter(prefix= "/auth", tags=["auth"])    # definindo prefixo padrao da rota
                                            # Ex:    https://dominio/AUTH/caminho definido a partir daqui


#   PARA CRIAÇÃO DE ROTAS
    # Estrutura da rota:
        # @ = decorator (usado para definir que é uma rota) | auth_router = variável que atribuimos o APIRouter | .get = metodo aser utilizado (get, post, put,etc ..) | ("/") = caminho do endpoint  

@auth_router.get("/")
async def home():
        
        """
        Essa é a rota padrão de autenticação do nosso sistema
        """
        return {"mensagem":"Você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str):
        
        Sesion = sessionmaker(bind=db) # criando sessão de banco de dados
        session = Sesion() # instanciando sessão
        usuario = session.query(Usuario).filter(Usuario.email == email).first() # verificando se o email já existe no banco de dados
        if usuario:
                return {"mensagem": "Email já cadastrado"}
        else:
                novo_usuario = Usuario(nome, email, senha) # criando novo usuário
                session.add(novo_usuario) # adicionando novo usuário na sessão
                session.commit() # salvando alterações no banco de dados    
                return {"mensagem": "Usuário cadastrado com sucesso"}
