# Projeto 04 — Assistente com Memória (IA Generativa)

Assistente conversacional simples em **Python** que demonstra conceitos fundamentais de aplicações com **IA generativa**, incluindo gerenciamento de memória, persona do assistente, integração com funções Python e persistência de histórico.

---

## Funcionalidades

* **Controle de memória da conversa**

  * Histórico de mensagens mantido durante a execução
  * Comando `/limpar` apaga a memória da conversa

* **Persona do assistente**

  * Mensagem de sistema define o comportamento e tom das respostas

* **Limite de memória**

  * Mantém apenas as **últimas 10 mensagens**
  * Mensagens mais antigas são removidas automaticamente

* **Integração com funções Python**

  * Execução automática de funções quando necessário
  * Exemplos implementados:

    * Gerador de senha segura
    * Consulta de data atual

* **Persistência de dados**

  * Histórico salvo em `conversation.json`
  * Conversa é restaurada ao reiniciar o programa

---

## Estrutura do Projeto

```
projeto04/
│
├── main.py              # Execução do assistente
├── tools.py             # Funções auxiliares (ex: gerar senha, data atual)
├── memory_manager.py    # Gerenciamento de memória da conversa
├── conversation.json    # Histórico persistente
└── README.md
```

---

## Como Executar

### 1. Criar ambiente virtual (opcional)

```bash
python -m venv venv
```

Ativar:

Linux / Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### 2. Executar o projeto

A partir da pasta raiz do repositório:

```bash
python projeto04/main.py
```

---

## Exemplo de Uso

```
Você: olá
Assistente: Olá! Como posso ajudar você hoje?

Você: gerar senha
Assistente: Sua senha é: X8#pL2mQ!
```

Limpar memória:

```
/limpar
```

---

## Tecnologias

* Python 3
* JSON para persistência de dados

---

## Objetivo

Demonstrar conceitos básicos de construção de **assistentes conversacionais com memória e ferramentas externas**, aplicando práticas de organização de código e persistência de dados.

## Reflexões e dificuldades encontradas

A implementação foi feita com base no código disponibilizado, apenas sendo necessário adaptar os trechos para usar no Groq. Depois, com ajuda de IA generativa, desenvolvi a estrutura base do projeto, com um arquivo memory_manager.py e um conversation.json.

* Se o histórico crescer muito, quais problemas podem ocorrer no uso de LLMs?
A LLM pode se perder, exemplo, se eu mandar um prompt dizendo que meu nome é Alan e depois dizer que meu nome é João, isso vai salvar no mesmo histórico dentro do projeto04, e aí como o robô vai diferenciar quem tá falando só com base em um histórico JSON.

* Por que algumas tarefas são melhores resolvidas por funções Python do que pelo próprio LLM?
Isso foi um aprendizado para mim da última aula, pois nunca havia pensado nisso, que a LLM tem capacidade de chamar uma função em Python, ao menos nas LLMs mais novas. É melhor usar isso justamente pra não precisar reinventar a roda, já que existe uma função que faz o trabalho muito bem, mais rápido e as vezes até melhor que o robô, por conta dos arredondamentos e alunicação.

* Quais riscos existem ao deixar que o LLM tome decisões sobre quando usar uma função?
Cheguei à conclusão após pesquisa, mas há riscos de prompt injection se o usuário malicioso induzir o LLM chamar funções que não deveria.