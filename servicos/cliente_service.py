from entidades.cliente_entidade import Cliente
from database.db import Session
from sqlalchemy import update, delete


class Cliente_service():
    def __init__(self):
        self.session = Session()
        
    def cadastro_cliente(self, nome , cpf , telefone , email):
        try:
            cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
            self.session.add(cliente)
            self.session.commit()
            print("Cliente cadastrado com sucesso!")
        except SQLAlchemyError as e:
            print("Erro ao cadastrar o cliente no banco de dados:", e)
        except Exception as e:
            print("Ocorreu um erro inesperado:", e)  
 
    def listar_cliente(self):

        try: 
            
            clientes = self.session.query(Cliente).all()
            if len(clientes)<1:
                print('Não possuimos nenhum cliente cadastrado no momento!/n Tente novamente mais tarde! :()')
            else:    
                for cliente in clientes:
                    print(f'ID_Cliente:{cliente.id_cliente} | nome: {cliente.nome} | cpf: {cliente.cpf} | telefone: {cliente.telefone} | email: {cliente.email}')
        except SQLAlchemyError as e:
            print('Erro ao listar os clientes do banco de dados', e) 
        except Exception as e:
            print('Ocorreu um erro inesperado:' , e)           

    def update_cliente(self, id_cliente,nome,cpf,telefone,email):
        try:
            query_cliente = self.session.query(Cliente).where(Cliente.id_cliente == id_cliente).first()   
            if not query_cliente:
                print('Cliente não existe')
            else:
                query=(
                    update(Cliente)
                    .where(Cliente.id_cliente==id_cliente)
                    .values(nome=nome,cpf=cpf,telefone=telefone,email=email)
                    )      
                self.session.execute(query)
                self.session.commit()

        except SQLAlchemyError as e:
            print('Erro ao atualizar o cliente no banco de dados', e) 
        except Exception as e:
            print('Ocorreu um erro inesperado:' , e)                
            


    def delete_cliente(self, id_cliente):
        try:
            query = delete(Cliente).where(Cliente.id_cliente==id_cliente)
            if not query_cliente:

            self.session.execute(query)
            self.session.commit()



            print("Cliente deletado com sucesso")

        
        except SQLAlchemyError as e:
                print('Erro ao deletar o(s) cliente(s) do banco de dados', e) 
        except:
                print('Ocorreu um erro inesperado:')           
  


    