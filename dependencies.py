from fastapi import Depends
from models import db      # importando modelo de usuario para criar conta
from sqlalchemy.orm import sessionmaker, Session # importando sessionmaker para criar sessão de banco de dados  
from models import Usuario



def pegar_sessao():

    try:
        Session = sessionmaker(bind=db) # criando sessão de banco de dados
        session = Session() # instanciando sessão
        yield session
    finally:
        session.close() # fechando sessão após uso


def verificar_token(token, session: Session = Depends(pegar_sessao)):
        #verificar se o token é válido
        #caso valido, extrai o id do usuario do token
        usuario = session.query(Usuario).filter(Usuario.id==1).first() 
        return usuario