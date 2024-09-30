# Introdução
Este é um projeto de exemplo para demonstrar a utilização do Git e do GitHub.

# Executando o projeto

<p>Para executar o projeto, siga os seguintes passos:</p>

## 1. Criar virtualenv
```bash
python -m venv .venv
```

## 2. Ativar virtualenv
```bash 
source .venv/bin/activate
```

## 3. Instalar dependências
Caso você esteja usando macOS, primeiro instale pkg-config e mysql-client através do Brew e exporte a variável PKG_CONFIG_PATH antes de instalar as dependências. Essa etapa não é obrigatória em outros sistemas operacionais.

```bash
brew install mysql-client
brew install pkg-config
export PKG_CONFIG_PATH="/opt/homebrew/opt/mysql-client/lib/pkgconfig"
```

A seguir, instale as dependências através do pip:

```bash
pip install -r requirements.txt
```

## 4. Executar o projeto no modo local
```bash
python manage.py runserver
```