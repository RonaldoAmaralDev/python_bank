# 🟦 BANK - Sistema Bancário em Python

Sistema bancário em terminal com funcionalidades completas:

- Criação de contas de clientes
- Depósitos e saques
- Consulta de saldo
- Extrato detalhado
- Máscara de CPF enquanto digita
- Máscara de telefone (residencial ou celular) enquanto digita
- Banco de dados SQLite integrado

---

## Estrutura do projeto

```
python_bank/
├── main.py               # Arquivo principal que inicia o sistema
├── menu.py               # Menu principal e menu do cliente
├── database.py           # Inicialização e conexão SQLite
├── movimentacoes.py      # Funções de movimentação e extrato
├── clientes.py           # Funções de criação e busca de clientes
├── utils.py              # Funções auxiliares (limpar tela, pausa, formatar dinheiro, input CPF, input telefone)
├── schema.sql            # Script SQL para criar tabelas
└── .venv/                # Ambiente virtual Python
```

---

## Pré-requisitos

- Python 3.10 ou superior
- WSL (Windows Subsystem for Linux) ou Linux
- SQLite3

---

## Configuração no WSL

1. Navegue até o diretório do projeto:

```bash
cd ~/projetos/python_bank
```

2. Criar e ativar o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependências (se houver `requirements.txt`):

```bash
pip install -r requirements.txt
```

4. Inicializar banco de dados

O banco SQLite (`bank.db`) será criado automaticamente na primeira execução, com as tabelas:

- `clientes`
- `movimentacoes`

---

## Executando o sistema

```bash
python main.py
```

### Exemplo de execução

```
🟦 BANK - Sistema Bancário
1 - Criar nova conta
2 - Acessar conta
3 - Sair
👉 Escolha: 1
👤 Nome: Ronaldo Amaral
🆔 CPF: 123.456.756-00
🏠 Endereço: Rua Teste
📞 Telefone: (31) 91231-4569
✅ Conta criada com sucesso! ID: 1
👉 A - Acessar conta | B - Voltar: A

🟦 BANK - Conta Corrente
👤 Cliente: Ronaldo Amaral
🆔 Conta:   1
💰 Saldo:   R$ 0,00

[A] Depositar
[B] Sacar
[C] Extrato
[D] Sair
👉 Escolha:
```

- **Depósito**: permite adicionar valor à conta
- **Saque**: retira valor se houver saldo suficiente
- **Extrato**: lista todas as movimentações

---

## Máscara de CPF

- O CPF será exibido no formato `000.000.000-00` enquanto o usuário digita.
- O valor armazenado no banco é apenas os números (`12345675600`).

## Máscara de Telefone

- Telefones residenciais: `(XX) XXXX-XXXX`
- Telefones celulares: `(XX) 9XXXX-XXXX`
- Retorna apenas números para armazenamento.

---

## Formatando valores monetários

- O saldo e extrato usam `locale` para formatar em reais.
- Se ocorrer erro de locale no WSL:

```bash
sudo apt update
sudo apt install language-pack-pt
sudo locale-gen pt_BR.UTF-8
sudo update-locale
```

- Fallback: caso a locale não funcione, o formato será `R$ 1.234,56`.

---

## Testando o sistema

1. Criar 2 contas
2. Fazer depósitos e saques
3. Consultar saldo e extrato
4. Tentar sacar valor maior que o saldo (deve exibir erro)
5. Acessar contas por ID

---

## Observações

- Sistema modular: fácil de estender
- Banco de dados SQLite local (`bank.db`)
- Indicado rodar em terminal Linux ou WSL

---

## Comandos úteis

- Limpar tela (WSL/Linux): `Ctrl+L`
- Sair do Python: `Ctrl+D`
- Recriar banco: deletar `bank.db` e rodar `python main.py`

## Backlog

- Padronização dos nomes em inglês para melhor clareza do código
- Acesso por número da agência e conta (sem IDs internos)
- Senha ao criar conta para maior segurança
- Validador de CPF integrado no cadastro
- Buscador de endereço por CEP para preencher dados automaticamente
- Opção de imprimir extrato diretamente no terminal
- Interface gráfica para facilitar o uso
- Histórico completo de transações
- Relatórios em PDF
- Integração com SQLite para persistência de dados


