from sqlalchemy.exc import SQLAlchemyError
from servicos.cliente_service import Cliente_service
from servicos.veiculo_service import Veiculo_service
from servicos.venda_service import Venda_service
from database.db import init_db

# Inicia o banco de dados
init_db()

def solicitar_dado(tipo, mensagem, obrigatorio=True, defaultValue=None):
    while True:
        try:
            valor = input(mensagem) if defaultValue is None else input(mensagem + f" [{defaultValue}] ")
            if obrigatorio and not valor:
                raise ValueError("Valor fornecido vazio")
            if defaultValue is not None and not valor:
                return defaultValue
            return tipo(valor)
        except ValueError as e:
            print(f"{e}, informe um {tipo.__name__} válido.")

def listagemSubmenu(cliente_service, veiculo_service, venda_service):
    print("\n===== Menu de Opções =====")
    print("1 - Listar Clientes")
    print("2 - Listar Veículos disponiveis")
    print("3 - Listar Veiculo")
    print("4 - Listar Vendas")
    print("5 - Listar Venda especifica")
    print("6 - Nenhuma das anteriores")
    print("==========================")
    opcao = input("Escolha uma opção:  ")

    if opcao == '1':
        cliente_service.listar_clientes()
        
    elif opcao == '2':
        veiculo_service.lista_veiculos_disponiveis()
        
    elif opcao == '3':
        id_veiculo = solicitar_dado(int, "Digite o ID do veiculo: ")
        veiculo_service.selecionar_veiculo_por_id(id_veiculo)
        
    elif opcao == '4':
        venda_service.listar_vendas()
        
    elif opcao == '5':
        id_venda = solicitar_dado(int, "Digite o ID da venda: ")
        venda_service.listar_venda(id_venda)
        
    elif opcao == '6':
        pass
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def cadastroSubmenu(cliente_service, veiculo_service, venda_service):
    print("\n===== Menu de Opções =====")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Veículo")
    print("3 - Realizar uma venda")
    print("4 - Nenhuma das anteriores")
    print("==========================")
    opcao = input("Escolha uma opção:  ")

    if opcao == '1':
        nome = solicitar_dado(str, "Digite o nome do cliente: ")
        cpf = solicitar_dado(str, "Digite o CPF do cliente: ")
        telefone = solicitar_dado(str, "Digite o telefone do cliente: ")
        email = solicitar_dado(str, "Digite o email do cliente: ")
        
        while True:
            if len(cpf) < 11:
                print("O CPF deve ter 11 dígitos.")
                cpf = solicitar_dado(str, "Digite o CPF do cliente: ")
            if len(telefone) < 11:
                print("O telefone deve ter 11 dígitos.")
                telefone = solicitar_dado(str, "Digite o telefone do cliente: ")
            else:
                break
            
        cliente_service.cadastro_cliente(nome, cpf, telefone, email)
        
    elif opcao == '2':
        marca = solicitar_dado(str, "Digite a marca do veiculo: ")
        modelo = solicitar_dado(str, "Digite o modelo do veiculo: ")
        ano = solicitar_dado(str, "Digite o ano do veiculo: ")
        preco = solicitar_dado(float, "Digite o preco do veiculo: ")
        cor = solicitar_dado(str, "Digite a cor do veiculo: ")
        numero_de_rodas = solicitar_dado(int, "Digite o numero de rodas do veiculo: ")
        placa = solicitar_dado(str, "Digite a placa do veiculo: ")
        
        veiculo_service.cadastro_veiculo(marca, modelo, ano, preco, cor, numero_de_rodas, placa)
        
    elif opcao == '3':
        id_cliente = solicitar_dado(int, "Digite o ID do cliente: ")
        id_veiculo = solicitar_dado(int, "Digite o ID do veiculo: ")
        venda_service.cadastro_venda(id_cliente, id_veiculo)
        
    elif opcao == '4':
        pass
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def deletarSubmenu(cliente_service, veiculo_service):
    print("\n===== Menu de Opções =====")
    print("1 - Deletar Cliente")
    print("2 - Deletar Veículo")
    print("3 - Nenhuma das anteriores")
    print("==========================")
    opcao = input("Escolha uma opção:  ")

    if opcao == '1':
        id_cliente = solicitar_dado(int, "Digite o ID do cliente: ")
        cliente_service.delete_cliente(id_cliente)
        
    elif opcao == '2':
        id_veiculo = solicitar_dado(int, "Digite o ID do veiculo: ")
        veiculo_service.deleta_veiculo(id_veiculo)
        
    elif opcao == '3':
        pass
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def atualizarSubmenu(cliente_service, veiculo_service):
    print("\n===== Menu de Opções =====")
    print("1 - Atualizar dados de Cliente")
    print("2 - Atualizar dados do Veículo")
    print("3 - Nenhuma das anteriores")
    print("==========================")
    opcao = input("Escolha uma opção:  ")

    if opcao == '1':
        id_cliente = solicitar_dado(int, "Digite o ID do cliente: ")
        cliente = cliente_service.selecionar_cliente_pelo_id(id_cliente)
        
        if cliente:
            nome = solicitar_dado(str, "Digite o nome do cliente ou pressione Enter para manter a atual: ", False, defaultValue=cliente.nome)
            cpf = solicitar_dado(str, "Digite o CPF do cliente ou pressione Enter para manter a atual: ", False, defaultValue=cliente.cpf)
            telefone = solicitar_dado(str, "Digite o telefone do cliente ou pressione Enter para manter a atual: ", False, defaultValue=cliente.telefone)
            email = solicitar_dado(str, "Digite o email do cliente ou pressione Enter para manter a atual: ", False, defaultValue=cliente.email)
            
            while True:
                if len(cpf) < 11:
                    print("O CPF deve ter 11 dígitos.")
                    cpf = solicitar_dado(str, "Digite o CPF do cliente: ")
                if len(telefone) < 11:
                    print("O telefone deve ter 11 dígitos.")
                    telefone = solicitar_dado(str, "Digite o telefone do cliente: ")
                else:
                    break
            
            cliente_service.atualizar_cliente(id_cliente, nome, cpf, telefone, email)
        else:
            pass
        
    elif opcao == '2':
        id_veiculo = solicitar_dado(int, "Digite o ID do veiculo: ")
        veiculo = veiculo_service.selecionar_veiculo_por_id(id_veiculo)
        
        if veiculo:
            marca = solicitar_dado(str, "Digite a nova marca do veiculo ou pressione Enter para manter a atual: ", False, defaultValue=veiculo.marca)
            modelo = solicitar_dado(str, "Digite o novo modelo do veiculo ou pressione Enter para manter o atual: ", False, defaultValue=veiculo.modelo)
            ano = solicitar_dado(str, "Digite o novo ano do veiculo ou pressione Enter para manter o atual: ", False, defaultValue=veiculo.ano)
            preco = solicitar_dado(float, "Digite o novo preco do veiculo ou pressione Enter para manter o atual: ", False, defaultValue=veiculo.preco)
            cor = solicitar_dado(str, "Digite a nova cor do veiculo ou pressione Enter para manter a atual: ", False, defaultValue=veiculo.cor)
            numero_de_rodas = solicitar_dado(int, "Digite o novo numero de rodas do veiculo ou pressione Enter para manter o atual: ", False, defaultValue=veiculo.numero_de_rodas)
            placa = solicitar_dado(str, "Digite a nova placa do veiculo ou pressione Enter para manter a atual: ", False, defaultValue=veiculo.placa)
            
            veiculo_service.atualiza_veiculo(
                id_veiculo,
                marca,
                modelo,
                ano,
                preco,
                cor,
                numero_de_rodas,
                placa
            )
        else:
            pass
    elif opcao == '3':
        pass
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def menu():
    cliente_service = Cliente_service()
    veiculo_service = Veiculo_service()
    venda_service = Venda_service()
    
    while True:
        print("\n===== Menu Principal =====")
        print("1 - Cadastro")
        print("2 - Listagem")
        print("3 - Atualização")
        print("4 - Deletar")
        print("5 - Sair")
        print("==========================")
        opcao = input("Escolha uma opção:  ")

        if opcao == '1':
            cadastroSubmenu(cliente_service, veiculo_service, venda_service)
        elif opcao == '2':
            listagemSubmenu(cliente_service, veiculo_service, venda_service)
        elif opcao == '3':
            atualizarSubmenu(cliente_service, veiculo_service)
        elif opcao == '4':
            deletarSubmenu(cliente_service, veiculo_service)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if(__name__ == "__main__"):
    menu()