# Handler Archive CNAB

***A API faz o cadastro de clientes, com os campos Nome, CPF e Nascimento. Além de fazer a validação do CPF com algorítmo com as regras contidas no link: https://www.macoratti.net/alg_cpf.htm#:~:text=O.***


## Tecnologias Utilizadas

- **Python**
- **Django**
- **Rest_Framework**
- **PostgreSQL**
- **SQLite**
- **CI - Testes**
- **Gunicorn**
- **Docker**


# Rodando a aplicação

Copie o arquivo  `.env.example` para o `.env` e forneça as credenciais do banco de dados que deseja usar

1. Rode os containers com o docker compose:
	```
	docker compose up
	```
	ou

	```
	docker-compose up
	```

**A aplicação estará rodando na porta 8000**

## Rodando em ambiente de produção

1. Primeiro, crie o arquivo `.env` 

2.  Crie o ambiente virtal:

	```
	python -m venv venv
	```
3. Ative seu venv:

	 *No Linux:*
	```
	source venv/bin/activate
	```
	*No windows:*
	```
	.\venv\Scripts\activate
	```
4. Instale as dependências do projeto: 
	```
	pip install -r requirements.txt
	```
5. Em settings.py do projeto defina `DEBUG=True` e rode o comando `python manage.py collectstatic` para gerar os arquivos estáticos.

6. Rode o projeto:
  ```
  python manage.py runserver
  ```
  ou com gunicorn
	```
  export DJANGO_SETTINGS_MODULE=api_clients.settings
	gunicorn -c gunicorn.conf.py api_clients.wsgi:application
	```
## Para rodar os testes##:
```
TEST=TEST python manage.py test
```
