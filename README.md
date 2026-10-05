# 🤖 Chatbot com Python, Streamlit e Gemini

Um chatbot desenvolvido em **Python** utilizando **Streamlit** para a interface e a API do **Google Gemini** para geração das respostas.

O projeto foi criado com o objetivo de estudar e praticar conceitos de desenvolvimento de aplicações com Inteligência Artificial, integração com APIs e gerenciamento de estado em aplicações Streamlit.

## 🚀 Tecnologias utilizadas

* 🐍 Python
* 🎈 Streamlit
* ✨ Google Gemini API
* 🔐 Variáveis de ambiente
* 💬 Chat com histórico de mensagens

## 📌 Funcionalidades

Atualmente, o chatbot possui:

* Interface de chat utilizando Streamlit
* Envio de mensagens para o modelo Gemini
* Recebimento e exibição das respostas da IA
* Histórico das mensagens durante a sessão
* Separação entre mensagens do usuário e do chatbot

## 📂 Estrutura do projeto

```text
chatbot/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/pollyanarocha416/chat-bot-ai.git
```

Entre na pasta:

```bash
cd chat-bot
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual.

No Windows:

```bash
venv\Scripts\activate
```

No Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

> ⚠️ Nunca publique sua API Key no GitHub.

Adicione o `.env` ao `.gitignore`:

```text
.env
venv/
__pycache__/
```

### 5. Execute o projeto

```bash
streamlit run app.py
```

Após executar, o Streamlit disponibilizará a aplicação no navegador.

## 💬 Exemplo

O usuário pode enviar uma pergunta:

```text
Olá! O que é Python?
```

E o chatbot utilizará o Gemini para gerar uma resposta.

## 🔮 Próximas melhorias

Algumas funcionalidades que podem ser implementadas futuramente:

* Restringir o chatbot a um assunto específico
* Adicionar uma personalidade ao chatbot
* Melhorar o gerenciamento do histórico
* Permitir limpar a conversa
* Adicionar upload de arquivos
* Fazer perguntas utilizando o conteúdo dos arquivos
* Implementar RAG (Retrieval-Augmented Generation)
* Adicionar banco de dados
* Criar autenticação de usuários
* Adicionar diferentes modelos de IA
* Registrar perguntas e respostas
* Criar uma interface mais personalizada
* Fazer deploy da aplicação

## 🎯 Objetivo do projeto

Este projeto faz parte dos estudos sobre **Python, desenvolvimento web e Inteligência Artificial**, explorando como integrar modelos de linguagem em aplicações reais.

## 👩‍💻 Autora

**P**
