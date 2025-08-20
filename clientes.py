from datetime import datetime
from database import conectar

def criar_cliente(nome, cpf, endereco, telefone):
    with conectar() as conn:
        conn.execute("""
            INSERT INTO clientes (nome, cpf, endereco, telefone, criado_em)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, cpf, endereco, telefone, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()
        return conn.execute("SELECT last_insert_rowid()").fetchone()[0]

def buscar_cliente(cliente_id):
    with conectar() as conn:
        cur = conn.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
        row = cur.fetchone()
        if row:
            return dict(zip([c[0] for c in cur.description], row))
    return None