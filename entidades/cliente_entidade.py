from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Cliente(Base):
    __tablename__ = "Clientes"
    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String,nullable=False)
    cpf=Column(String,nullable=False)
    telefone=Column(String,nullable=False)
    email=Column(String,nullable=False)
    def __repr__(self):
        return f'<Cliente:(nome={self.nome}, id_cliente={self.id_cliente}, cpf={self.cpf}, telefone={self.telefone}, email={self.email})>'