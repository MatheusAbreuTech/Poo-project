from entidades.cliente_entidade import Cliente
from database.db import Session
from sqlalchemy import update, delete, exc
from plyer import notification
import time

class Cliente_service():
    def __init__(self):
        self.session = Session()

    def cadastro_cliente(self, nome , cpf , telefone , email):
        try:
            cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
            self.session.add(cliente)
            self.session.commit()

            notification.notify(
                title = "PERFEITO!!!",
                message = "Cliente cadastrado com sucesso!",
                timeout = 1000
            )
        except exc.SQLAlchemyError as e:
            print(f"Error ao cadastrar o cliente no banco de dados!: {e}")
        except Exception as e:
            print("Ocorreu um erro inesperado!: " + str(e))

    def listar_clientes(self):
        try:
            clientes = self.session.query(Cliente).all()
            if len(clientes)<1:
                notification.notifly(
                    title = "ERROR",
                    message = "Não possuimos cliente cadastrado no momento! \n Tente novamente mais tarde!:",
                    timeout = 1000
                )
            else:
                for cliente in clientes:
                    print(f'ID_Cliente:{cliente.id_cliente} | nome: {cliente.nome} | cpf: {cliente.cpf} | telefone: {cliente.telefone} | email: {cliente.email}')

        except exc.SQLAlchemyError as e:
            print(f"Erro ao listar os clientes do banco de dados {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
    
    def selecionar_cliente_pelo_id(self, id_cliente):
        try:
            cliente = self.session.query(Cliente).where(Cliente.id_cliente == id_cliente).first()
            if not cliente:
                notification.notify(
                    title = "ERROR",
                    message = "Cliente nao encontrado!",
                    timeout = 1000
                )
            else:
                print(f'ID_Cliente:{cliente.id_cliente} | nome: {cliente.nome} | cpf: {cliente.cpf} | telefone: {cliente.telefone} | email: {cliente.email}')
                return cliente
        except exc.SQLAlchemyError as e:
            print(f"Erro ao listar o cliente no banco de dados {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualizar_cliente(self, id_cliente,nome,cpf,telefone,email):
        try:
            query_cliente = self.session.query(Cliente).where(Cliente.id_cliente == id_cliente).first()
            if not query_cliente:
                notification.notify(
                    title = "ERROR",
                    message = "Cliente não existente",
                    timeout = 1000
                )
            else:
                query=(
                    update(Cliente)
                    .where(Cliente.id_cliente==id_cliente)
                    .values(nome=nome,cpf=cpf,telefone=telefone,email=email)
                    )
                self.session.execute(query)
                self.session.commit()
                notification.notify(
                    title = "PERFEITO!!!",
                    message = "Cliente atualizado com sucesso!",
                    timeout = 1000
                )
        except exc.SQLAlchemyError as e:
            print(f"Erro ao arualizar o cliente no banco de dados {e}")
        except Exception as e:
            print(f"Occoreu um erro inesperado: {e}")

    def delete_cliente(self, id_cliente):
        try:
            cliente = self.session.query(Cliente).where(Cliente.id_cliente == id_cliente).first()
            if cliente:
                query = (delete(Cliente).where(Cliente.id_cliente==id_cliente))
                self.session.execute(query)
                self.session.commit()
                notification.notify(
                    title = "PERFEITO!!!",
                    message = "Cliente deletado com sucesso!",
                    timeout = 1000
                )
            else:
                notification.notify(
                    title = "ERROR",
                    message = "Cliente nao encontrado!",
                    timeout = 1000
                )
        except exc.SQLAlchemyError as e:
            print(f"Error ao deletar o(s) cliente(s) do banco de dados {e}")

        except Exception as e:
            print(f"Occoreu um erro inesperado: {e}",)