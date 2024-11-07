from sqlalchemy.exc import SQLAlchemyError
from servicos.cliente_service import Cliente_service
from servicos.veiculo_service import Veiculo_service
from servicos.venda_service import Venda_service

from database.db import init_db

# Inicia o banco de dados
init_db()

def mostrar_menu():
    print("\n===== Menu de Opções =====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Veículos")
    print("3 - Deletar Cliente")
    print("4 - Deletar Veículo")
    print("5 - Deletar Venda")
    print("6 - Cadastrar Veículo")
    print("7 - Realizar uma venda")
    print("8 - Listar Clientes")
    print("9 - Atualizar dados de Cliente")
    print("10 - Nenhuma das anteriores")
    print("==========================")

def dizer_ola():
    print("Olá, usuário!")

def main():
    cliente_service = Cliente_service()
    veiculo_service = Veiculo_service()
    venda_service = Venda_service()
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção:  ")

        if opcao == '1':
            print('Perfeito! Nos forneça alguns dados:') 
            nome = input('Nome: ')
            cpf = int(input('CPF: '))  # CPF como string para manter zeros à esquerda
            telefone = int(input('Telefone: '))
            email = input('E-mail: ')

            cliente_service.cadastro_cliente(nome, cpf, telefone, email)
      

        elif opcao == '2':
            print('Esses são os veículos que possuímos:')
            veiculo_service.lista_veiculos()

        elif opcao == '3':
            cliente_a_deletar = int(input('Qual cliente deseja deletar?: '))

            cliente_service.delete_cliente(cliente_a_deletar)
            # try:
            # except SQLAlchemyError as e:
            #     print('Error ao deletar o cliente do banco de dados:' , e)
            # except Exception as e:
            #     print('Ocorreu um erro inesperado!' , e)

        elif opcao == '4':
            veiculo_a_deletar = int(input('Qual veículo deseja deletar: '))
            veiculo_service.deleta_veiculo(veiculo_a_deletar)
            
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
                "placa": placa,
                "disponivel": 1
            }
            veiculo_service.cadastro_veiculo(**veiculo_dados)
            
        elif opcao == '7':
            # implementar
            pass
        
        elif opcao=='8':
            print('Esses são os clientes que possuimos:')
            cliente_service.listar_cliente()

        elif opcao=='9':
            print('Perfeito! Nos forneça alguns dados')
            id=int(input('ID do cliente: '))
            nome=input("Nome:")
            cpf=int(input('CPF: '))
            telefone=int(input("Telefone: "))
            email=input("Email: ")
            cliente_service.update_cliente(id,nome,cpf,telefone,email)





        elif opcao == '10':
            print("Saindo... Obrigado por usar o programa!")                           
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal diretamente
main()
