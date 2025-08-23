# 🏦 Python Bank

Um projeto simples de **banco digital em Python** para estudos, simulação e prática de programação orientada a objetos.  

O objetivo é simular operações bancárias como criação de contas, depósitos, saques e transferências, utilizando boas práticas de código e estrutura clara.

---

## ✨ Novidades desta versão

- 🔤 **Padronização dos nomes em inglês** para melhor clareza do código  
- 🏦 **Acesso por número da agência e conta** (sem IDs internos)  
- 🔒 **Senha ao criar conta** para maior segurança  
- ✅ **Validador de CPF integrado** no cadastro  

---

## 🚀 Funcionalidades

- Criar conta com **nome, CPF, agência, conta e senha**  
- Listar contas cadastradas  
- Depositar valores  
- Sacar valores com senha de autenticação  
- Transferir entre contas existentes  
- Validar CPF antes de criar uma nova conta  

---

## 📂 Estrutura do Projeto

python_bank/
├── bank.py # Classe principal do banco
├── account.py # Classe que representa a conta bancária
├── cpf_validator.py # Função para validação de CPF
├── main.py # Ponto de entrada do programa
└── README.md # Documentação do projeto

## 🛠️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/RonaldoAmaralDev/python_bank.git
Entre na pasta do projeto:

cd python_bank
Execute o programa:

python main.py
🧪 Exemplo de Uso
Ao rodar o programa, você poderá:

===== Python Bank =====
1 - Criar conta
2 - Listar contas
3 - Depositar
4 - Sacar
5 - Transferir
0 - Sair

✅ Criar conta → informa nome, CPF válido e senha
✅ Depositar → adiciona saldo
✅ Sacar → exige senha correta
✅ Transferir → de uma conta para outra

📌 Próximos Passos
📊 Relatórios de movimentações da conta

💾 Persistência dos dados (SQLite ou JSON)

🌐 Criar versão com interface web (Flask/Django ou FastAPI)

🧑‍💻 Implementar testes unitários

🤝 Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.
Sugestões são sempre bem-vindas! 🚀

📄 Licença
Este projeto está sob a licença MIT.
