# Escola Online de Tecnologia

## Proof Of Concept (POC)

### Execução do projeto:

Instalar o Python (Versão de projeto: 3.10.4)

Acessar a pasta do POC do repositório clonado = [/poc/poc2]

Criar um ambiente virtual por meio do comando: `py -m venv venv`

Ativar o ambiente virtual: `venv/Scripts/activate` (Windows) ou `source venv/bin/activate` (Linux/macOS)

Instalar os requerimentos do projeto, presentes no arquivo [requirements.txt]: `pip install -r requirements.txt`

#### Em caso de erro durante a instalação dos pacotes presentes em 'requirements.txt', pode ser necessário realizar mudança da versão do gerenciador de pacotes do Python por meio do comando: ``py -m pip install pip=21` (versão que se mostrou funcional, inicialmente).

Acessar o diretório /loja

Realizar o migrate das tabelas para o banco de dados: `py manage.py makemigrations` seguido de `py manage.py migrate`

Iniciar o servidor local: `py manage.py runserver`

Acessar o projeto em navegador por meio da porta 8000 = [localhost:8000]