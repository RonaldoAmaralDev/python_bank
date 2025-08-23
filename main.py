from account import Account
from cpf_validator import validate_cpf

accounts = []

def create_account():
    name = input("Digite seu nome: ").strip()
    cpf = input("Digite seu CPF: ").strip()
    
    if not validate_cpf(cpf):
        print("❌ CPF inválido.")
        return

    agency = "0001"
    number = str(len(accounts) + 1001)
    password = input("Crie uma senha: ").strip()
    
    account = Account(name, cpf, agency, number, password)
    accounts.append(account)
    
    print(f"✅ Conta criada com sucesso! Agência: {agency} | Número: {number}")

def find_account(agency: str, number: str, password: str):
    for acc in accounts:
        if acc.agency == agency and acc.number == number and acc.password == password:
            return acc
    return None

def access_account():
    agency = input("Digite sua agência: ").strip()
    number = input("Digite o número da conta: ").strip()
    password = input("Digite sua senha: ").strip()
    
    account = find_account(agency, number, password)
    
    if account:
        print(f"✅ Bem-vindo(a) {account.name}!")
        account_menu(account)
    else:
        print("❌ Credenciais inválidas.")

def main_menu():
    while True:
        print("\n===== Python Bank =====")
        print("1 - Criar conta")
        print("2 - Acessar conta")
        print("3 - Listar contas")
        print("0 - Sair")
        choice = input("Escolha uma opção: ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            access_account()
        elif choice == "3":
            for acc in accounts:
                print(f"{acc.name} | {acc.agency}-{acc.number} | Saldo: R$ {acc.balance:.2f}")
        elif choice == "0":
            break
        else:
            print("⚠️ Opção inválida.")

def account_menu(account: Account):
    while True:
        print("\n--- Menu da Conta ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Mostrar saldo")
        print("4 - Histórico de transações")
        print("5 - Transferir para outra conta")
        print("0 - Sair")
        choice = input("Escolha uma opção: ").strip()
        
        if choice == "1":
            amount = float(input("Digite o valor para depósito: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Digite o valor para saque: "))
            password = input("Digite sua senha: ").strip()
            account.withdraw(amount, password)
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            target_agency = input("Digite a agência da conta destino: ").strip()
            target_number = input("Digite o número da conta destino: ").strip()
            target_account = None
            for acc in accounts:
                if acc.agency == target_agency and acc.number == target_number:
                    target_account = acc
                    break
            if not target_account:
                print("❌ Conta destino não encontrada.")
                continue
            amount = float(input("Digite o valor para transferência: "))
            password = input("Digite sua senha: ").strip()
            account.transfer(amount, target_account, password)
        elif choice == "0":
            break
        else:
            print("⚠️ Opção inválida.")

if __name__ == "__main__":
    main_menu()