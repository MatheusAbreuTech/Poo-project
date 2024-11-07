from entidades.venda_entidade import Venda
from entidades.veiculo_entidade import Veiculo
from entidades.cliente_entidade import Cliente

from database.db import Session
from sqlalchemy import update, delete, select

class Venda_service():
    def __init__(self):
        self.session = Session()
        
    def cadastro_venda (self, id_veiculos , id_cliente , data_venda , valor_total):
        query_cliente = self.session.query(Cliente).where(Cliente.id_cliente == id_cliente).first()
        query_veiculo = self.session.query(Veiculo).where(Veiculo.id_veiculo == id_veiculos).first()

        if not query_cliente:
            print(f'O Cliente {id_cliente} não existe')
        elif not query_veiculo:
            print(f'O Veiculo {id_veiculos} não está disponível')
        else:
            cadastro = Venda(Cliente=query_cliente , Veiculo=query_veiculo , data_venda=data_venda , valor_total=valor_total)
            self.session.add(cadastro)
            self.session.commit()

    def delete_venda(self, id_venda):
        query=delete(Venda).where(Venda.id_venda==id_venda)
        session.execute(query)
        session.commit()

    def update_venda(self, id_venda,id_veiculo,veiculo,id_cliente,Cliente,data_venda,valor_total):
        query=(
            update(Venda)
            .where(Venda.id_venda==id_venda)
            .values(id_veiculo=id_veiculo,veiculo=veiculo,id_cliente=id_cliente,Cliente=Cliente,data_venda=data_venda,valor_total=valor_total)
            )
        self.session.execute(query)
        self.session.commit()

    # perguntar pro matheus<-- não esta trazendo os valores
    def lista_vendas(self):
        vendas= self.session.query(Venda).all()
        for venda in vendas:
            print(f'id da venda: {Venda.id_venda}')
            print(f'Veiculo: {Venda.Veiculo}')
            print(f'Cliente: {Venda.Cliente}')
            print(f'Data-Hora: {Venda.data_venda}')
            print(f'Valor-total: {Venda.valor_total}')