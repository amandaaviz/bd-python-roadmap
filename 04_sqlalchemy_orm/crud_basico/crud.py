from database import SessionLocal
from models import Cliente

session = SessionLocal()

# Create
novo = Cliente(nome="Amanda Aviz", email="amanda@exemplo.com", cidade="Belém")
session.add(novo)
session.commit()

# Read
clientes = session.query(Cliente).all()
for c in clientes:
    print(c.id, c.nome)

# Update
cliente = session.query(Cliente).filter_by(id=1).first()
cliente.cidade = "Ananindeua"
session.commit()

# Delete
session.delete(cliente)
session.commit()

session.close()
