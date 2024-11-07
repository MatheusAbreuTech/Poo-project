from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float, update, delete, select
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from entidades import Veiculo_service, Cliente_service, Venda_service, Veiculo, Venda, Cliente

# Configuração do engine para conexão com o banco de dados SQLite
engine = create_engine('sqlite:///biblioteca.db')

def mostrar_menu():
    print("\n===== Menu de Opções =====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Veículos")
    print("3 - Deletar Cliente")
    print("4 - Deletar Veículo")
    print("5 - Deletar Venda")
    print("6 - Cadastrar Veículo")
    print("7 - Realizar uma venda")
    print("8 - Nenhuma das anteriores")
    print("==========================")

def dizer_ola():
    print("Olá, usuário!")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção:  ")

        if opcao == '1':
            print('Perfeito! Nos forneça alguns dados:') 
            nome = input('Nome: ')
            cpf = input('CPF: ')  # CPF como string para manter zeros à esquerda
            telefone = input('Telefone: ')
            email = input('E-mail: ')

            Session = sessionmaker(bind=engine)
            session = Session()

            try:
                # Tenta cadastrar o cliente
                Cliente_service.cadastro_cliente(nome, cpf, telefone, email)
                
                # Verifica se o cliente foi cadastrado com sucesso no banco de dados
                cliente_cadastrado = session.query(Cliente).filter_by(cpf=cpf).first()
                
                if cliente_cadastrado:
                    print("Cliente cadastrado com sucesso!")
                else:
                    print("Erro: Não foi possível cadastrar o cliente.")
                    
            except SQLAlchemyError as e:
                print("Erro ao cadastrar o cliente no banco de dados:", e)
                
            except Exception as e:
                print("Ocorreu um erro inesperado:", e)
                
            finally:
                session.close()

        elif opcao == '2':
            print('Esses são os veículos que possuímos:')
            Veiculo_service.lista_veiculos()

            
        elif opcao == '3':
            cliente_a_deletar = int(input('Qual cliente deseja deletar?: '))
            
            
            Session = sessionmaker(bind=engine)
            session = Session()

            try:
                cliente_deletado = session.query(Cliente).filter_by(id_cliente==id_cliente).first()

                if cliente_deletado:
                    Cliente_service.delete_cliente(cliente_a_deletar)
                    print('Cliente deletado com sucesso!')
                else:
                    print('Error: Nãi foi possível deletar o cliente')
            except SQLAlchemyError as e:
                print('Error ao deletar o cliente do banco de dados:' , e)
            except Exception as e:
                print('Ocorreu um erro inesperado!' , e)

            finally:
                session.close()
                

            
        elif opcao == '4':
            veiculo_a_deletar = int(input('Qual veículo deseja deletar: '))
            Veiculo_service.delete_veiculos(veiculo_a_deletar)
            
        elif opcao == '5':
            venda_a_deletar = int(input('Qual venda deseja deletar?: '))
            Venda_service.delete_venda(venda_a_deletar)
            
        elif opcao == '6':
            marca = input("Marca do veículo: ")
            modelo = input("Modelo do veículo: ")
            ano = input("Ano do veículo: ")
            preco = float(input("Preço do veículo: "))
            cor = input("Cor do veículo: ")
            numero_de_rodas = int(input("Número de rodas do veículo: "))
            placa = input("Placa do veículo: ")

            # Cria o dicionário para enviar os dados
            veiculo_dados = {
                "marca": marca,
                "modelo": modelo,
                "ano": ano,
                "preco": preco,
                "cor": cor,
                "numero_de_rodas": numero_de_rodas,
                "placa": placa
            }
            Veiculo_service.cadastro_veiculo(**veiculo_dados)
            
        elif opcao == '7':
            id_veiculo = int(input("ID do veículo: "))
            id_cliente = int(input("ID do cliente: "))
            nome_cliente = input("Nome do cliente: ")
            data_venda = input("Data da venda (AAAA-MM-DD): ")
            valor_total = float(input("Valor total: "))

            venda_dados = {
                "id_veiculo": id_veiculo,
                "id_cliente": id_cliente,
                "nome_cliente": nome_cliente,
                "data_venda": data_venda,
                "valor_total": valor_total
            }
            Venda_service.realizar_venda(**venda_dados)
            
        elif opcao == '8':
            print("Saindo... Obrigado por usar o programa!")                           
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal diretamente
main()

# Executa o programa
#main()
