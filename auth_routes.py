from fastapi import APIRouter, Depends, HTTPException       # importando roteador
from models import Usuario      # importando modelo de usuario para criar conta
from dependencies import pegar_sessao # importando função para pegar sessão de banco de dados
from main import bcrypt_context # importando contexto de criptografia para senhas do main.py


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
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
        usuario = session.query(Usuario).filter(Usuario.email==email).first() # verificando se o email já existe no banco de dados
        if usuario:
                raise HTTPException(status_code=400, detail="Email já cadastrado")      # se o email já existir, retorna um erro 400 (Bad Request) com a mensagem "Email já cadastrado" 
        else:
                senha_criptografada = bcrypt_context.hash(senha) # criptografando a senha utilizando o contexto de criptografia definido no main.py             
                novo_usuario = Usuario(nome, email, senha_criptografada) # criando novo usuário
                session.add(novo_usuario) # adicionando novo usuário na sessão
                session.commit() # salvando alterações no banco de dados    
                return {"mensagem": "Usuário cadastrado com sucesso"}
