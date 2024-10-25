from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Date,Float,update,delete
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine= create_engine('sqlite:///biblioteca.db')
Session=sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "Clientes"
    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String,nullable=False)
    cpf=Column(Integer,nullable=False)
    telefone=Column(Float,nullable=False)
    email=Column(String,nullable=False)
    def __repr__(self):
        return f'<Cliente: (nome={self.nome}, ID={self.id_cliente})>'


    
       
class Venda(Base):
    __tablename__ = "Vendas"
    id_venda = Column(Integer, primary_key=True)
    id_veiculo = Column(Integer, ForeignKey('Veiculos.id_veiculo'))
    Veiculo = relationship('Veiculo', backref='Vendas')
    id_cliente = Column(Integer, ForeignKey('Clientes.id_cliente'))
    Cliente = relationship('Cliente', backref='Vendas')
    nome = Column(String, nullable=False)
    carro = Column(String,nullable=False)
    cliente = Column(String,nullable=False)
    data_venda=Column(Date,nullable=False)
    valor_total=Column(Float,nullable=False)
    def __repr__(self):
        return f'<Id Venda: (nome={self.id_venda}, Valor={self.valor_total})>'
    

   
class Veiculo(Base):

    __tablename__ = "Veiculos"
    id_veiculo = Column(Integer, primary_key=True)
    marca = Column(String, nullable=False)
    modelo=Column(String, nullable=False)
    ano=Column(Integer, nullable=False)
    preco=Column(Float, nullable=False)
    cor=Column(String, nullable=False)
    numero_de_rodas=Column(Integer, nullable=False)

    placa=Column(String, nullable=False)

    def __repr__(self):
        return f'<Id Veiculos: (nome={self.id_veiculo}, Marca={self.marca} , Modelo={self.modelo} , Ano={self.ano} , Preço={self.preco} , Cor={self.cor} , Numero de rodas={self.numero_de_rodas} ,    Placa={self.placa} )>'

Base.metadata.create_all(engine)        


class Veiculo_service():
    def cadastro_veiculo(marca,modelo,ano,preco,cor,numero_de_rodas,placa):
       veiculo = Veiculo(marca=marca,modelo=modelo,ano=ano,preco=preco,cor=cor,numero_de_rodas=numero_de_rodas,placa=placa)
       session.add(veiculo)
       session.commit()
       
    def lista_veiculos():
        
        veiculos = session.query(Veiculo).all()
        for veiculo in veiculos:
            print(veiculo.marca)
            print(veiculo.modelo)
            print(veiculo.ano)
            print(veiculo.preco)
            print(veiculo.cor)
            print(veiculo.numero_de_rodas)
            print(veiculo.placa)


    def uptade_veiculos(id_veiculo,marca, modelo,ano,preco,cor,numero_de_rodas,placa):
        query=(
            update(Veiculo)
            .where(Veiculo.id_veiculo==id_veiculo)
            .values(marca=marca,modelo=modelo,ano=ano,preco=preco,cor=cor,numero_de_rodas=numero_de_rodas,placa=placa)
            )
        session.execute(query) 
        session.commit()


    def delete_veiculos(id_veiculo):
        query=delete(Veiculo).where(id_veiculo==id_veiculo)
        print(query)
        session.execute(query)
        session.commit()    
        
class Cliente_service():
    def cadastro_cliente(nome , cpf , telefone , email):
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
        session.add(cliente)
        session.commit()          
 
    def listar_cliente():
        
        clientes = session.query(Cliente).all()
        for cliente in clientes:
            print(cliente.nome)

    def update_cliente(id_cliente,nome,cpf,telefone,email):
        query=(
            update(Cliente)
            .where(Cliente.id_cliente==id_cliente)
            .values(nome=nome,cpf=cpf,telefone=telefone,email=email)
            )
        session.execute(query)
        session.commit()

    def delete_cliente(id_cliente):
        query = delete(Cliente).where(id_cliente==id_cliente)
        print(query)
        session.execute(query)
        session.commit()
