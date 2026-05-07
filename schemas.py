from pydantic import BaseModel      # Importando a classe BaseModel do módulo pydantic, que é usada para criar modelos de dados para validação e serialização.
from typing import Optional     # Importando a classe Optional do módulo typing, que é usada para indicar que um campo é opcional em um modelo de dados.

class UsuarioSchema(BaseModel):     # Criando a classe UsuarioSchema que herda de BaseModel, essa classe será usada para definir a estrutura dos dados de um usuário, incluindo os campos nome, email, senha, ativo e admin. Os campos ativo e admin são opcionais, o que significa que eles podem ser omitidos ao criar um novo usuário.
    nome: str
    email: str
    senha: str
    ativo: Optional[bool] 
    admin: Optional[bool] 

    class Config:
        from_attributes = True      # Configurando a classe Config para permitir a criação de instâncias do modelo a partir de objetos que possuem atributos correspondentes aos campos definidos no modelo. Isso é útil para facilitar a conversão de objetos do banco de dados em instâncias do modelo, permitindo que os dados sejam validados e serializados corretamente.


class PedidoSchema(BaseModel):  
    usuario_id: int

    class Config:
        from_attributes = True