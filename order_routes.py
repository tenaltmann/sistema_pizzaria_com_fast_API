from fastapi import APIRouter, Depends       # importando roteador
from sqlalchemy.orm import Session # importando Session do SQLAlchemy para tipagem da sessão de banco de dados
from dependencies import pegar_sessao # importando função para pegar sessão de banco de dados
from schemas import PedidoSchema # importando schema de pedido para validação dos dados de entrada
from models import Pedido # importando modelo de pedido para criar instância do pedido no banco de dados


order_router = APIRouter(prefix= "/order", tags=["pedidos"])    # definindo prefixo padrao da rota
                                              # Ex:    https://dominio/ORDER/caminho definido a partir daqui

#   PARA CRIAÇÃO DE ROTAS
    # Estrutura da rota:
        # @ = decorator (usado para definir que é uma rota) | order_router = variável que atribuimos o APIRouter | .get = metodo aser utilizado (get, post, put,etc ..) | ("/") = caminho do endpoint  

@order_router.get("/")
async def pedidos():
        
        """
        Essa é a rota padrão de pedidos do nosso sistema

        """
        return {"mensagem":"Você acessou a rota de pedidos"}

@order_router.get("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
        novo_pedido = Pedido(usuario=PedidoSchema.usuario_id) # Criando uma nova instância do modelo Pedido, passando o ID do usuário obtido do schema de pedido.
        session.add(novo_pedido) # Adicionando o novo pedido à sessão do banco de dados.
        session.commit() # Comitando a sessão para salvar as alterações no banco de dados.
        return {"mensagem": f"Pedido criado com sucesso! ID do pedido: {novo_pedido.id}"} # Retornando uma mensagem de sucesso para indicar que o pedido foi criado com sucesso.    

