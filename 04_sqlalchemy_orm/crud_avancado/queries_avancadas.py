from database import SessionLocal
from models import Cliente, Pedido
from sqlalchemy import func

session = SessionLocal()

# Todos os pedidos de um cliente específico
cliente = session.query(Cliente).filter_by(nome="João Silva").first()
for pedido in cliente.pedidos:
    print(pedido.valor)

# Clientes com pedidos acima de 200
clientes = session.query(Cliente).join(Pedido).filter(Pedido.valor > 200).all()
for c in clientes:
    print(c.nome)

# Soma de todos os pedidos por cliente
somas = session.query(Cliente.nome, func.sum(Pedido.valor)).join(Pedido).group_by(Cliente.id).all()
for nome, total in somas:
    print(f"{nome}: R$ {total}")

session.close()
