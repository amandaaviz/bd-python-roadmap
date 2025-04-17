from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# URL para SQLite (pode trocar para MySQL depois)
DATABASE_URL = "sqlite:///meu_banco.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Cria as tabelas com base nos models
Base.metadata.create_all(bind=engine)
