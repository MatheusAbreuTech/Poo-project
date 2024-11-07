from entidades.veiculo_entidade import Veiculo
from database.db import Session
from sqlalchemy import update, delete, select

class Veiculo_service():
    def __init__(self):
        self.session = Session()
        
    def cadastro_veiculo(self, marca,modelo,ano,preco,cor,numero_de_rodas,placa , disponivel):
       veiculo = Veiculo(marca=marca,modelo=modelo,ano=ano,preco=preco,cor=cor,numero_de_rodas=numero_de_rodas,placa=placa , disponivel=disponivel)
       self.session.add(veiculo)
       self.session.commit()
       
    def lista_veiculos(self):
        veiculos = self.session.query(Veiculo).all()
        for veiculo in veiculos:
            print(veiculo.marca)
            print(veiculo.modelo)
            print(veiculo.ano)
            print(veiculo.preco)
            print(veiculo.cor)
            print(veiculo.numero_de_rodas)
            print(veiculo.placa)

    def atualiza_veiculo(self, id_veiculo,marca, modelo,ano,preco,cor,numero_de_rodas,placa):
        query=(
            update(Veiculo)
            .where(Veiculo.id_veiculo==id_veiculo)
            .values(marca=marca,modelo=modelo,ano=ano,preco=preco,cor=cor,numero_de_rodas=numero_de_rodas,placa=placa)
            )
        self.session.execute(query) 
        self.session.commit()

    def deleta_veiculo(self, id_veiculo):
        query=delete(Veiculo).where(id_veiculo==id_veiculo)
        self.session.execute(query)
        self.session.commit()    

    def selecionar_veiculo_por_id(self, id_veiculo):
        query=(
            select(Veiculo)
            .where(Veiculo.id_veiculo==id_veiculo)
            )
        self.session.execute(query)
        self.session.commit()