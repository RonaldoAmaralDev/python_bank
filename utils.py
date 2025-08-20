import os
import locale
import sys
import tty
import termios

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("⚠️ Locale pt_BR.UTF-8 não disponível. Usando locale padrão.")
    locale.setlocale(locale.LC_ALL, '')

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def formatar_dinheiro(valor):
    try:
        return locale.currency(valor, grouping=True)
    except ValueError:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def pausa():
    input("\n🔁 Pressione Enter para continuar...")

def input_valor(msg: str):
    try:
        valor = float(input(msg).replace(",", "."))
        if valor > 0:
            return valor
        print("❌ Valor inválido.")
    except ValueError:
        print("❌ Entrada inválida.")
    return None

def input_cpf(prompt="🆔 CPF: "):
    print(prompt, end="", flush=True)
    cpf = ""
    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if ch in ("\r", "\n"):  
            print()
            break
        elif ch == "\x7f": 
            if len(cpf) > 0:
                cpf = cpf[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        elif ch.isdigit():
            cpf += ch
            display = ""
            for i, c in enumerate(cpf):
                if i in [3, 6]:
                    display += "." + c
                elif i == 9:
                    display += "-" + c
                else:
                    display += c
            sys.stdout.write("\r" + prompt + display)
            sys.stdout.flush()

    return cpf

def input_telefone(prompt="📞 Telefone: "):
    import sys, tty, termios

    print(prompt, end="", flush=True)
    telefone = ""
    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if ch in ("\r", "\n"):  
            print()
            break
        elif ch == "\x7f":  
            if len(telefone) > 0:
                telefone = telefone[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        elif ch.isdigit():
            telefone += ch
            display = ""
            for i, c in enumerate(telefone):
                if i == 0:
                    display += "(" + c
                elif i == 1:
                    display += c + ") "
                elif i == 2 and len(telefone) <= 10:
                    display += c
                elif i == 3 and len(telefone) <= 10:
                    display += c
                elif i == 4 and len(telefone) <= 10:
                    display += c
                elif i == 5 and len(telefone) <= 10:
                    display += c + "-"
                elif i == 2 and len(telefone) > 10:
                    display += "9" + c
                elif i == 6 and len(telefone) > 10:
                    display += c + "-"
                else:
                    display += c
            sys.stdout.write("\r" + prompt + display)
            sys.stdout.flush()

    return telefone