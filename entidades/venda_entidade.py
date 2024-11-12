from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database.db import Base

class Venda(Base):
    __tablename__ = "Vendas"
    id_venda = Column(Integer, primary_key=True)
    id_veiculo = Column(Integer, ForeignKey('Veiculos.id_veiculo'))
    Veiculo = relationship('Veiculo', backref='Vendas')
    id_cliente = Column(Integer, ForeignKey('Clientes.id_cliente'))
    Cliente = relationship('Cliente', backref='Vendas')
    data_venda=Column(DateTime,nullable=False)
    valor_total=Column(Float,nullable=False)
    def __repr__(self):
        return f'<Id Venda: (id_venda={self.id_venda}, id_veiculo={self.id_veiculo}, Veiculo={self.Veiculo}, id_cliente={self.id_cliente}, Cliente={self.Cliente}, data_venda={self.data_venda}, valor_total={self.valor_total})>'