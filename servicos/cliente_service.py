from entidades.cliente_entidade import Cliente
from database.db import Session
from sqlalchemy import update, delete


class Cliente_service():
    def __init__(self):
        self.session = Session()
        
    def cadastro_cliente(self, nome , cpf , telefone , email):
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
        self.session.add(cliente)
        self.session.commit()
 
    def listar_cliente(self):
        clientes = self.session.query(Cliente).all()
        for cliente in clientes:
            print(cliente.nome)
            print(cliente.cpf)
            print(cliente.telefone)
            print(cliente.email)

    def update_cliente(self, id_cliente,nome,cpf,telefone,email):
        query=(
            update(Cliente)
            .where(Cliente.id_cliente==id_cliente)
            .values(nome=nome,cpf=cpf,telefone=telefone,email=email)
            )
        self.ession.execute(query)
        self.session.commit()

    def delete_cliente(self, id_cliente):
        query = delete(Cliente).where(id_cliente==id_cliente)
        print(query)
        self.session.execute(query)
        self.session.commit()