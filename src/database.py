
"""
qui si crea l'accesso al database che vogliamo creare col nostro script
usando linguaggio / libreria SQl che gia contiene cio che ci serve
importiamo da SQl cio che ci serve e apriamo il nostro Database
(come aprire un json, lo devi aprire poi lavorarlo e poi chiuderlo)
uguale apriamo un database, poi con engine lo facciamo partire (come uvicorn per git)
poi con sessionmaker creiamo le sessioni di lavoro
ci lavoriamo dentro lo modifichiamo facciamo quello che ci serve con Base
la funzione GET no ci serve per prendere e modificare il database con una sicurezza
try/finally yield, yield itera e se durante le modifiche al database appare un errore
non modifica il database originale ma lo chiude
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""from src.config import DATABASE_URL sostituisce DATABASE_URL="sqlite:///./sql_app.db" """
from src.config import DATABASE_URL

# DATABASE_URL="sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



