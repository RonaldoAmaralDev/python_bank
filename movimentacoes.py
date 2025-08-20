from datetime import datetime
from database import conectar

def registrar_movimentacao(cliente_id, tipo, valor):
    with conectar() as conn:
        conn.execute("""
            INSERT INTO movimentacoes (cliente_id, tipo, valor, data)
            VALUES (?, ?, ?, ?)
        """, (cliente_id, tipo, valor, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()

def carregar_saldo(cliente_id):
    with conectar() as conn:
        cur = conn.execute("""
            SELECT tipo, valor FROM movimentacoes WHERE cliente_id = ?
        """, (cliente_id,))
        saldo = 0.0
        for tipo, valor in cur.fetchall():
            if "Depósito" in tipo or "recebida" in tipo:
                saldo += valor
            elif "Saque" in tipo or "enviada" in tipo:
                saldo -= valor
        return saldo

def extrato(cliente_id):
    with conectar() as conn:
        cur = conn.execute("""
            SELECT data, tipo, valor FROM movimentacoes
            WHERE cliente_id = ? ORDER BY id
        """, (cliente_id,))
        return cur.fetchall()