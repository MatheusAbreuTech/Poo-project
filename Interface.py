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
    print("2 - Cadastrar Veículo")
    print("3 - Realizar uma venda")
    print("4 - Atualizar dados de Cliente")
    print("5 - Atualizar dados do Veículo")
    print("6 - Listar Clientes")
    print("7 - Listar Veículos disponiveis")
    print("8 - Listar Veículo")
    print("9 - Listar Vendas")
    print("10 - Listar Venda especifica")
    print("11 - Deletar Cliente")
    print("12 - Deletar Veículo")
    print("13 - Nenhuma das anteriores")
    print("==========================")
    
def solicitar_dado(tipo, mensagem, obrigatorio=True):
    while True:
        try:
            valor = input(mensagem)
            if obrigatorio and not valor:
                raise ValueError("Valor fornecido vazio")
            return tipo(valor)
        except ValueError as e:
            print(f"{e}, informe um {tipo.__name__} válido.")

def main():
    cliente_service = Cliente_service()
    veiculo_service = Veiculo_service()
    venda_service = Venda_service()
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção:  ")

        if opcao == '1':
            print('Perfeito! Nos forneça alguns dados:') 

            nome = solicitar_dado(str, 'Nome: ')
            cpf = solicitar_dado(int, 'CPF: ')
            telefone = solicitar_dado(int, 'Telefone: ')
            email = solicitar_dado(str, 'E-mail: ')

            cliente_service.cadastro_cliente(nome, cpf, telefone, email)
            
        elif opcao == '2':
            marca = solicitar_dado(str, "Marca do veículo: ")
            modelo = solicitar_dado(str, "Modelo do veículo: ")
            ano = solicitar_dado(str, "Ano do veículo: ")
            preco = solicitar_dado(float, "Preço do veículo: ")
            cor = solicitar_dado(str, "Cor do veículo: ")
            numero_de_rodas = solicitar_dado(int, "Número de rodas do veículo: ")
            placa = solicitar_dado(str, "Placa do veículo: ")

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
        elif opcao == '3':
            id_veiculo = solicitar_dado(int, "Forneça o ID do veículo: ")
            id_cliente = solicitar_dado(int, "Forneça o ID do cliente que deseja comprar o carro: ")
            
            venda_service.cadastro_venda(id_veiculo, id_cliente)
        elif opcao=='4':
            print('Perfeito! Nos forneça alguns dados')
            id_cliente=solicitar_dado(int, 'ID do cliente: ')
            nome=solicitar_dado(str, "Nome:")
            cpf=solicitar_dado(int, 'CPF: ')
            telefone=solicitar_dado(int, "Telefone: ")
            email=solicitar_dado(str, "Email: ")

            cliente_service.update_cliente(id_cliente,nome,cpf,telefone,email)

        elif opcao == '5':
            print('Esses são os clientes que possuimos:')
            cliente_service.listar_cliente()

        elif opcao == '6':
            print('Esses são os veículos que possuemos:')
            veiculo_service.lista_veiculos()

        elif opcao == '7':
            cliente_a_deletar = solicitar_dado(int, 'Qual cliente deseja deletar?: ')

            cliente_service.delete_cliente(cliente_a_deletar)

        elif opcao == '8':
            veiculo_a_deletar = solicitar_dado(int, 'Qual veículo deseja deletar: ')
            veiculo_service.deleta_veiculo(veiculo_a_deletar)
            
        elif opcao == '9':
            venda_a_deletar = solicitar_dado(str,'Qual venda deseja deletar?: ')
            Venda_service.delete_venda(venda_a_deletar)
        
        elif opcao == '10':
            print("Saindo... Obrigado por usar o programa!")                           
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal diretamente
main()
