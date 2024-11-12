from entidades.cliente_entidade import Cliente
from database.db import Session
from sqlalchemy import update, delete

import notification , time

class Cliente_service():
    def __init__(self):
        self.session = Session()
        
    def cadastro_cliente(self, nome , cpf , telefone , email):
        try:
             while True:   
                cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
                self.session.add(cliente)
                self.session.commit()
                
                notification.notify(
                    title = "PERFEITO!!!",
                    message = "Cliente cadastrado com sucesso!",
                    timeout = 10
                )
                time.sleep(3600)
        except SQLAlchemyError as e:
            notification.notify(
                title = "ERROR",
                menssage = f"Error ao cadastrar o cliente no banco de dados!: {e}",
                timeout = 10
            )
            time.sleep(3600)
        except Exception as e:
            notification.notify(
                title = "ERROR",
                menssage = f"Ocorreu um erro inesperado!: {e}",
                timeout = 10
            )
            time.sleep(3600)


 
    def listar_cliente(self):
        try: 
            while True:
                clientes = self.session.query(Cliente).all()
                if len(clientes)<1:
                    notification.notifly(
                        title = "ERROR",
                        menssage = "Não possuimos cliente cadastrado no momento! \n Tente novamente mais tarde!:",
                        timeout = 10
                    )
                    time.sleep(3600)
                else:    
                    for cliente in clientes:
                        print(f'ID_Cliente:{cliente.id_cliente} | nome: {cliente.nome} | cpf: {cliente.cpf} | telefone: {cliente.telefone} | email: {cliente.email}')
        except SQLAlchemyError as e:
            notification.notifly(
                title = "ERROR",
                menssage = f"Erro ao listar os clientes do banco de dados {e}",
                timeout = 10
            )
            time.sleep(3600)
        except Exception as e:
            notification.notifly(
                title = "ERROR",
                menssage = f"Ocorreu um erro inesperado",
                timeout = 10
            )
            time.sleep(3600)



    def update_cliente(self, id_cliente,nome,cpf,telefone,email):
        try:
            query_cliente = self.session.query(Cliente).where(Cliente.id_cliente == id_cliente).first()   
            if not query_cliente:
                notification.notify(
                    title = "ERROR",
                    menssage = "Cliente não existente",
                    timeout = 10
                )
                time.sleep(3600)
            else:
                query=(
                    update(Cliente)
                    .where(Cliente.id_cliente==id_cliente)
                    .values(nome=nome,cpf=cpf,telefone=telefone,email=email)
                    )      
                self.session.execute(query)
                self.session.commit()
        except SQLAlchemyError as e:
            notification.notify(
                title = "ERROR",
                menssage = f"Erro ao arualizar o cliente no banco de dados {e}",
                timeout  = 10
            )
            time.sleep(3600)
        except Exception as e:
            notification.notify(
                title = "ERROR",
                menssage = f"Occoreu um erro inesperado",
                timeout = 10
            )
            time.sleep(3600)
            


    def delete_cliente(self, id_cliente):
        try:
            query = delete(Cliente).where(Cliente.id_cliente==id_cliente)
            if not query_cliente:
                self.session.execute(query)
                self.session.commit()
                notification.notify(
                    title = "PERFEITO!!!",
                    menssage = "Cliente deletado cm sucesso!",
                    timeout = 10
                )
                time.sleep(3600)
        except SQLAlchemyError as e:
                notification.notify(
                    title = "ERROR",
                    menssage = f"Error ao deletar o(s) cliente(s) do banco de dados {e}",
                    timeout = 10
                )
                time.sleep(3600)
        except:
                notification.notify(
                    title = "ERROR",
                    menssage = f"Ocorreu um erro inesperado:",
                    timeout = 10
                )
                time.sleep(3600)
  


    