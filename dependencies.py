from models import Usuario, db      # importando modelo de usuario para criar conta
from sqlalchemy.orm import sessionmaker # importando sessionmaker para criar sessão de banco de dados  

def pegar_sessao():

    try:
        Session = sessionmaker(bind=db) # criando sessão de banco de dados
        session = Session() # instanciando sessão
        yield session
    finally:
        session.close() # fechando sessão após uso