from fastapi import Depends, HTTPException
from models import db      # importando modelo de usuario para criar conta
from sqlalchemy.orm import sessionmaker, Session # importando sessionmaker para criar sessão de banco de dados  
from models import Usuario
from main import ALGORITHM, SECRET_KEY, oauth2_schema # importando contexto de criptografia e variáveis de ambiente do main.py para utilização na criação de token e autenticação de usuário
from jose import JWTError, jwt # importando JWTError e jwt da biblioteca jose para criação e verificação de tokens JWT


def pegar_sessao():

    try:
        Session = sessionmaker(bind=db) # criando sessão de banco de dados
        session = Session() # instanciando sessão
        yield session
    finally:
        session.close() # fechando sessão após uso


def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
        try:
            dic_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            id_usuario = dic_info.get("sub") # extraindo o id do usuário do token decodificado
        except JWTError as erro:
            print(erro)
            raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do seu token") # se o token for inválido, retorna um erro 401 (Unauthorized) com a mensagem "Acesso Negado,verifique a validade do seu token"    
        
        #verificar se o token é válido
        #caso valido, extrai o id do usuario do token
        usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first() 
        if not usuario:
            raise HTTPException(status_code=401, detail="Acesso Inválido") # se o usuário não existir, retorna um erro 401 (Unauthorized) com a mensagem "Acesso Inválido"
        return usuario