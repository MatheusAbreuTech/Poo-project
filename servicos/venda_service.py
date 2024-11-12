from entidades.venda_entidade import Venda
from entidades.veiculo_entidade import Veiculo
from entidades.cliente_entidade import Cliente

from database.db import Session
from sqlalchemy import update, delete, select, exc
from plyer import notification
from servicos.veiculo_service import Veiculo_service
from datetime import datetime
import time

class Venda_service():
    def __init__(self):
        self.session = Session()
        self.veiculo_service = Veiculo_service()

    def cadastro_venda (self, id_veiculo , id_cliente):
        try:
            query_cliente = self.session.query(Cliente).where(Cliente.id_cliente == id_cliente).first()
            query_veiculo = self.session.query(Veiculo).where(Veiculo.id_veiculo == id_veiculo).first()

            if not query_cliente:
                notification.notify(
                    title = "CLIENTE NÃO EXISTE!!!",
                    message = f"O cliente {id_cliente} não existe!",
                    timeout = 1000
                )
            elif not query_veiculo:
                notification.notify(
                    title = "VEÍCULO NÃO EXISTE!!!",
                    message = f"O veículo {id_veiculo} não existe!",
                    timeout = 1000
                )
            elif query_veiculo.disponivel == 0:
                notification.notify(
                    title = "VEÍCULO INDISPONÍVEL!!!",
                    message = "Veículo não está disponível no momento!",
                    timeout = 1000
                )
            else:
                data_venda = datetime.now()
                cadastro = Venda(Cliente=query_cliente , Veiculo=query_veiculo , data_venda=data_venda , valor_total=query_veiculo.preco)
                self.session.add(cadastro)

                self.veiculo_service.mudar_disponibilidade_veiculo(id_veiculo, 0)
                self.session.commit()

                notification.notify(
                title = "PERFEITO!!!",
                message = "Venda realizada com sucesso!",
                timeout = 1000
                )

        except exc.SQLAlchemyError as e:
            self.session.rollback()
            print(f"Erro ao efetuar a venda {e}")
        except Exception as e:
            self.session.rollback()
            print(f"Ocorreu um erro inesperado: {e}")

    def listar_vendas(self):
        try:
            vendas = self.session.query(Venda).all()
            for venda in vendas:
                print(f"id da venda: {Venda.id_venda} | Veiculo: {Venda.Veiculo} | Cliente: {Venda.Cliente} | Data da venda: {Venda.data_venda} | Valor total: {Venda.valor_total}")
        except exc.SQLAlchemyError as e:
            print(f"Erro ao listar as vendas {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def listar_venda(self, id_venda):
        try:
            venda = self.session.query(Venda).where(Venda.id_venda == id_venda).first()
            print(f"id da venda: {Venda.id_venda} | Veiculo: {Venda.Veiculo} | Cliente: {Venda.Cliente} | Data da venda: {Venda.data_venda} | Valor total: {Venda.valor_total}")
        except exc.SQLAlchemyError as e:
            print(f"Erro ao listar a venda {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")