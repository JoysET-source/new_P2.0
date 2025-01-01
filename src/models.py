# """qui abbiamo creato la tabella users
#
# qui creiamo la funzione che creera usando il linguaggio sql la tabella degli users del nostro script
# importando dalla libreria sqlalchemy la struttura che ci serve (colonne, numeri, stringhe)
# poi importiamo dal file database da noi creato il linguaggio che creera questa tabella
# nella funzione diciamo a linguaggio SQL come si chiama la tabella che deve contenere (colonne numeri e stringhe)
#
# i modelli (models.py) non sono altro che gli object che noi vogliamo creare nel nostro database"""

"""nei modelli si mettono sempre prima gli import da librerie esterne e poi gli import dai nostri database interni"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

"""
questa e una tabella con 4 colonne (id, email, username, passwd), id si mette automatico
"""

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # questa aggiunta alla tabella user crea la correlazione bidirezionale con tabella todos
    todos = relationship("Todo", back_populates="user")

"""qui creiamo una tabella che si chiama todos come per user formata da 5 colonne
ultima voce user serve per mettere in correlazione le due tabelle todos e user
per creare tale correlazione importiamo da sql.orm la libreria relationship.
questa tabella la ritroviamo in datagrip con folder todos
osserva bene le cartelle perche cio che hai creato qui lo ritrovi li
inoltre osservando la tabella todo vediamo che la colonna id e user id
primary_key==chiave gialla
foreignKey==chiave blu"""

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="todos")




