from database import SessionLocal
from models import Cliente, Pedido

session = SessionLocal()

# Criar cliente com dois pedidos
cliente = Cliente(nome="João Silva", pedidos=[
    Pedido(valor=150.0),
    Pedido(valor=320.0)
])

session.add(cliente)
session.commit()
session.close()
