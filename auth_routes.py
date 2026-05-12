from fastapi import APIRouter, Depends, HTTPException       # importando roteador
from models import Usuario      # importando modelo de usuario para criar conta
from dependencies import pegar_sessao # importando função para pegar sessão de banco de dados
from main import bcrypt_context # importando contexto de criptografia para senhas do main.py
from schemas import UsuarioSchema, LoginSchema # importando schema de usuario para validação dos dados de entrada
from sqlalchemy.orm import Session # importando Session do SQLAlchemy para tipagem da sessão de banco de dados






auth_router = APIRouter(prefix= "/auth", tags=["auth"])    # definindo prefixo padrao da rota
                                            # Ex:    https://dominio/AUTH/caminho definido a partir daqui



#processo de criação de token PROVISÓRIO
def criar_token(id_usuario):
        token = f"agbdfnbdfnbsdfnb{id_usuario})"
        return token

def autenticar_usuario(email, senha, session):
        usuario = session.query(Usuario).filter(Usuario.email==email).first() # verificando se o email existe no banco de dados
        if not usuario:
                return False # se o email não existir, retorna False
        elif not bcrypt_context.verify(senha, usuario.senha):
                return False # se a senha estiver incorreta, retorna False
        return usuario




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
async def criar_conta(usuario_schema: UsuarioSchema  ,session: Session = Depends(pegar_sessao)):
        usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first() # verificando se o email já existe no banco de dados
        if usuario:
                raise HTTPException(status_code=400, detail="Email já cadastrado")      # se o email já existir, retorna um erro 400 (Bad Request) com a mensagem "Email já cadastrado" 
        else:
                senha_criptografada = bcrypt_context.hash(usuario_schema.senha) # criptografando a senha utilizando o contexto de criptografia definido no main.py

                novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin) # criando novo usuário

                session.add(novo_usuario) # adicionando novo usuário na sessão
                session.commit() # salvando alterações no banco de dados
                    
                return {"mensagem": f"Usuário cadastrado com sucesso {usuario_schema.email}"} 
        

#login -> email e senha -> token de autenticação (JWT) -> acesso as rotas protegidas do sistema
@auth_router.post("/login")
async def login( login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
        usuario = autenticar_usuario(login_schema.email, login_schema.senha, session) # autenticando usuário utilizando a função autenticar_usuario definida acima, passando o email, senha e sessão de banco de dados como parâmetros
        if not usuario:
                raise HTTPException(status_code=400, detail="Email ou senha incorretos") # se o email não existir, retorna um erro 400 (Bad Request) com a mensagem "Email ou senha incorretos"
        else:
                access_token = criar_token(usuario.id) # criando token de autenticação utilizando a função criar_token definida acima, passando o id do usuário como parâmetro
                return {
                        "access_token": access_token,     # retornando o token de autenticação para o cliente
                        "token_type": "bearer"              # informando o tipo do token (Bearer)
                        }
