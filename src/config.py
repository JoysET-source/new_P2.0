"""
in questo file scriviamo una funzione che prende i segreti contenuti
nel nostro database da .env e li trasmette al file database.py cosi
da tenerlo nascosto, cosi si puo usare ma non vedere
che se ci mettiamo le passwd rimangono nascoste

questa funzione prende le key da .env
poi la richiamiamo su database con (from src.config import DATABASE_URL)
se ritorna None da errore se no ritorna il valore della key (value = os.getenv(key))
"""

import os
from dotenv import load_dotenv

load_dotenv()

def get_env_or_raise(key: str) -> str:
    """ottieni una variabile o solleva un'eccezione"""
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"La variabile {key} is not set")
    return value

DATABASE_URL = get_env_or_raise("DATABASE_URL")
DATABASE_PASSWD = get_env_or_raise("DATABASE_PASSWD")
