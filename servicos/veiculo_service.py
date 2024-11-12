from entidades.veiculo_entidade import Veiculo
from database.db import Session
from sqlalchemy import update, delete, select
from plyer import notification
import time

class Veiculo_service():
    def __init__(self):
        self.session = Session()

    def cadastro_veiculo(self, marca,modelo,ano,preco,cor,numero_de_rodas,placa , disponivel):
       try:
            veiculo = Veiculo(marca=marca,modelo=modelo,ano=ano,preco=preco,cor=cor,numero_de_rodas=numero_de_rodas,placa=placa , disponivel=disponivel)
            self.session.add(veiculo)
            self.session.commit()
            notification.notify(
                title = "PERFEITO!!!",
                message = "Veículo cadastrado com sucesso",
                timeout = 1000
            )
       except SQLAlchemyError as e:
        print('Erro ao cadastrar o veiculo no banco de dados')
       except Exception as e:
        print("Ocorreu um erro inesperado")

    def lista_veiculos_disponiveis(self):
        try:
            veiculos = self.session.query(Veiculo).where(Veiculo.disponivel == 1).all()
            for veiculo in veiculos:
                print(f"Marca: {veiculo.marca} | Modelo: {veiculo.modelo} | Ano: {veiculo.ano} | Preço: {veiculo.preco} | Cor: {veiculo.cor} | Numero de rodas: {veiculo.numero_de_rodas} | Placa: {veiculo.placa}")
        except exc.SQLAlchemyError as e:
            print(f"Erro ao listar os veiculos {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualiza_veiculo(self, id_veiculo,marca, modelo,ano,preco,cor,numero_de_rodas,placa):
        try:
            query=(
                update(Veiculo)
                .where(Veiculo.id_veiculo==id_veiculo)
                .values(marca=marca,modelo=modelo,ano=ano,preco=preco,cor=cor,numero_de_rodas=numero_de_rodas,placa=placa)
                )
            self.session.execute(query)
            self.session.commit()

            notification.notify(
                title = "PERFETO!!!",
                message = "Veículo atualizado com sucesso!"
                timeout = 1000
            )
        except exc.SQLAlchemyError as e:
            print(f"Erro ao atualizar o veículo no banco de dados {e}")
        except Exception as e:
            print(f"Occoreu um erro inesperado: {e}")

    def mudar_disponibilidade_veiculo(self, id_veiculo, disponivel):
        try:
            query=(
                update(Veiculo)
                .where(Veiculo.id_veiculo==id_veiculo)
                .values(disponivel=disponivel)
                )
            self.session.execute(query)
            self.session.commit()
        except exc.SQLAlchemyError as e:
            print(f"Erro ao atualizar o veículo no banco de dados {e}")
        except Exception as e:
            print(f"Occoreu um erro inesperado: {e}")

    def deleta_veiculo(self, id_veiculo):
        try:
            query=delete(Veiculo).where(Veiculo.id_veiculo==id_veiculo)
            self.session.execute(query)
            self.session.commit()

            notification.notify(
                title = "DELETADO COM SUCESSO!!!",
                message = "Veículo deletado com sucesso!",
                timeout = 100
            )
        except exc.SQLAlchemyError as e:
            print(f"Error ao deletar o veiculo do banco de dados {e}")
        except Exception as e:
            print(f"Occoreu um erro inesperado: {e}")

    def selecionar_veiculo_por_id(self, id_veiculo):
        try:
            query=(
                select(Veiculo)
                .where(Veiculo.id_veiculo==id_veiculo)
                )
            self.session.execute(query)
            self.session.commit()
        except exc.SQLAlchemyError as e:
            print(f"Erro ao selecionar o veiculo no banco de dados {e}")
        except Exception as e:
            print(f"Occoreu um erro inesperado: {e}")