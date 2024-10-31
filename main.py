from entidades import Veiculo_service , Cliente_service , Venda_service

Veiculo_service.cadastro_veiculo('punto','fiat','1990','23000','azul','4','QKJD-2456' , '0')



Cliente_service.cadastro_cliente('Igor' , '04194240' , '112345678' , '123@gmail' )

# Cliente_service.listar_cliente()

# Veiculo_service.uptade_veiculos(1,'punto','chevrolet','1990','23000','azul','4','QKJD-2456')

# Veiculo_service.lista_veiculos()

# Cliente_service.update_cliente(1,'Jonatan' , '04194240' , '112345678' , '123@gmail')

# Cliente_service.delete_cliente(1)

Venda_service.cadastro_venda('1' , '1' , '2024-10-30 22:55:56.766940' , '102')