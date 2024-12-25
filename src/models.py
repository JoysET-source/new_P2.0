"""
qui abbiamo creato la tabella users

qui creiamo la funzione che creera usando il linguaggio sql la tabella degli users del nostro script
importando dalla libreria sqlalchemy la struttura che ci serve (colonne, numeri, stringhe)
poi importiamo dal file database da noi creato il linguaggio che creera questa tabella
nella funzione diciamo a linguaggio SQL come si chiama la tabella che deve contenere (colonne numeri e stringhe)

i modelli (models.py) non sono altro che gli object che noi vogliamo creare nel nostro database
"""

from sqlalchemy import Column, Integer, String
from src.database import Base

"""
questa e una tabella con 4 colonne (id, email, username, passwd)
"""

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

