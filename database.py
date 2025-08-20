import sqlite3

DB_PATH = "bank.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def inicializar():
    with conectar() as conn:
        with open("schema.sql", "r", encoding="utf-8") as f:
            conn.executescript(f.read())