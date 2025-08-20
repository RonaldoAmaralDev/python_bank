from utils import limpar_tela, pausa, formatar_dinheiro, input_valor, input_cpf, input_telefone
from clientes import criar_cliente, buscar_cliente
from movimentacoes import registrar_movimentacao, carregar_saldo, extrato

def menu_cliente(cliente_id):
    cliente = buscar_cliente(cliente_id)
    while True:
        limpar_tela()
        saldo = carregar_saldo(cliente_id)
        print("🟦 XPTO BANK - Conta Corrente")
        print(f"👤 Cliente: {cliente['nome']}")
        print(f"🆔 Conta:   {cliente['id']}")
        print(f"💰 Saldo:   {formatar_dinheiro(saldo)}")
        print("\n[A] Depositar\n[B] Sacar\n[C] Extrato\n[D] Sair")

        opcao = input("👉 Escolha: ").strip().upper()
        if opcao == "A":
            valor = input_valor("💰 Valor do depósito: R$ ")
            if valor:
                registrar_movimentacao(cliente_id, "Depósito", valor)
                print(f"✅ Depósito de {formatar_dinheiro(valor)} realizado.")
            pausa()

        elif opcao == "B":
            valor = input_valor("💸 Valor do saque: R$ ")
            if valor:
                if valor > saldo:
                    print("❌ Saldo insuficiente.")
                else:
                    registrar_movimentacao(cliente_id, "Saque", valor)
                    print(f"✅ Saque de {formatar_dinheiro(valor)} realizado.")
            pausa()

        elif opcao == "C":
            print("\n📄 Extrato da Conta:")
            for data, tipo, valor in extrato(cliente_id):
                print(f"{data} | {tipo:<25} | {formatar_dinheiro(valor)}")
            pausa()

        elif opcao == "D":
            print("👋 Saindo da conta...")
            break

        else:
            print("❌ Opção inválida.")
            pausa()

def menu_principal():
    while True:
        limpar_tela()
        print("🟦 XPTO BANK - Sistema Bancário")
        print("1 - Criar nova conta\n2 - Acessar conta\n3 - Sair")
        opcao = input("👉 Escolha: ").strip()

        if opcao == "1":
            nome = input("👤 Nome: ")
            cpf = input_cpf("🆔 CPF: ")
            endereco = input("🏠 Endereço: ")
            telefone = input_telefone("📞 Telefone: ")
            cliente_id = criar_cliente(nome, cpf, endereco, telefone)
            print(f"✅ Conta criada com sucesso! ID: {cliente_id}")
            if input("👉 A - Acessar conta | B - Voltar: ").strip().upper() == "A":
                menu_cliente(cliente_id)

        elif opcao == "2":
            cliente_id = input("🔑 ID da conta: ").strip()
            cliente = buscar_cliente(cliente_id)
            if cliente:
                menu_cliente(cliente_id)
            else:
                print("❌ Conta não encontrada.")
                pausa()

        elif opcao == "3":
            print("👋 Encerrando sistema.")
            break
        else:
            print("❌ Opção inválida.")
            pausa()