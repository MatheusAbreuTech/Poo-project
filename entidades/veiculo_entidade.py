from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Veiculo(Base):

    __tablename__ = "Veiculos"
    
    id_veiculo = Column(Integer, primary_key=True)
    marca = Column(String, nullable=False)
    modelo=Column(String, nullable=False)
    ano=Column(Integer, nullable=False)
    preco=Column(Float, nullable=False)
    cor=Column(String, nullable=False)
    numero_de_rodas=Column(Integer, nullable=False)
    disponivel=Column(Integer,nullable=False)
    placa=Column(String, nullable=False)

    def __repr__(self):
        return f'<Id Veiculos:(nome={self.id_veiculo}, marca={self.marca}, modelo={self.modelo}, ano={self.ano}, preco={self.preco}, cor={self.cor}, numero_de_rodas={self.numero_de_rodas}, placa={self.placa})>'
