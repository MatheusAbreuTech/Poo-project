from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Date,Float,update,delete,select
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from entidades import Veiculo_service,Cliente_service,Venda_service,Veiculo,Venda,Cliente

def mostrar_menu():
    print("\n===== Menu de Opções =====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Veiculos")
    print("3 - Deletar Cliente")
    print("4 - Deletar Veiculo")
    print("5 - Deletar Venda")
    print("6 - Cadastrar Veiculo")
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
            Cliente_service.cadastro_cliente()
        elif opcao == '2':
            print('Esses são os veiculos que possuimos:')
            Veiculo_service.lista_veiculos()
        elif opcao == '3':
            deleteado=input('Qual cliente deseja deletar?: ')
            Cliente_service.delete_cliente(deleteado)
        elif opcao == '4':
            valor=int(input('Qual veiculo deseja deletar:  '))
            Veiculo_service.delete_veiculos(valor)
        elif opcao == '5':
            valor=int(input('Qual venda deseja deletar?: '))
            Venda_service.delete_venda(valor)
        elif opcao == '6':
            veiculo=input(f'Perfeito!, nos forneça os seguintes valores: Marca: ( Marca={Veiculo.marca} , Modelo={Veiculo.modelo} , Ano={Veiculo.ano} , Preço={Veiculo.preco} , Cor={Veiculo.cor} , Numero de rodas={Veiculo.numero_de_rodas} ,    Placa={Veiculo.placa} )')
            Veiculo_service.cadastro_veiculo(veiculo)
        elif opcao == '7':
            venda=input(f'Perfeito!, nos forneça os seguintes valores: Id do veiculo:{Veiculo.id_veiculo}, ID do cliente:{Venda.id_cliente}, Nome do cliente:{Venda.Cliente},  Data da venda:{Venda.data_venda}, Valor total: {Venda.valor_total} '  )
                        
        elif opcao == '8':
            print("Saindo... Obrigado por usar o programa!")                           
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
