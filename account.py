from datetime import datetime

class Account:
    def __init__(self, name: str, cpf: str, agency: str, number: str, password: str):
        self.name = name
        self.cpf = cpf
        self.agency = agency
        self.number = number
        self.password = password
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            self.transactions.append({
                'tipo': 'Depósito',
                'valor': amount,
                'data': datetime.now()
            })
            print(f"✅ Depósito realizado: R$ {amount:.2f}")
        else:
            print("⚠️ Valor de depósito inválido.")

    def withdraw(self, amount: float, password: str):
        if password != self.password:
            print("❌ Senha incorreta.")
            return
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append({
                'tipo': 'Saque',
                'valor': amount,
                'data': datetime.now()
            })
            print(f"✅ Saque realizado: R$ {amount:.2f}")
        else:
            print("⚠️ Saldo insuficiente ou valor inválido.")

    def show_balance(self):
        print(f"💰 Saldo: R$ {self.balance:.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("📜 Nenhuma transação realizada ainda.")
            return

        print("📜 Histórico de transações:")
        for t in self.transactions:
            data = t['data'].strftime("%d/%m/%Y %H:%M:%S")
            tipo = t['tipo']
            valor = f"R$ {t['valor']:.2f}"
            
            if 'para' in t:
                print(f"{data} | {tipo} | {valor} | Para: {t['para']}")
            elif 'de' in t:
                print(f"{data} | {tipo} | {valor} | De: {t['de']}")
            else:
                print(f"{data} | {tipo} | {valor}")