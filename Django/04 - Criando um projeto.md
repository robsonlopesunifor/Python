Criando um projeto 

crie uma pasta para organizar os arquivos:

	robson@robson:~/Documentos$ mkdir pasta_do_projeto
	robson@robson:~/Documentos$ cd pasta_do_projeto

	robson@robson:~/Documentos/pasta_do_projeto$

cria o ambiente virtual-------------------------------------------------------------------------- 
	
	python3 -m venv nome_da_venv

	para ativar o ambiente virtual  

	robson@robson:~/Documentos/pasta_do_projeto$ 
linux
	source nome_da_venv/bin/activate

	(venv) robson@robson:~/Documentos/pasta_do_projeto$

Windows 
	cd venv/Scripts/activate
	(venv) robson@robson:~/Documentos/pasta_do_projeto/venv/Scripts/activate$
	(venv) robson@robson:~/Documentos/pasta_do_projeto/venv/Scripts/activate$ cd.. cd.. cd..
	(venv) robson@robson:~/Documentos/pasta_do_projeto$

Django: agora precisamos instalar o django no ambiente virtual ---------------------------------

	dentro do activate
	(venv) robson@robson:~/Documentos/pasta_do_projeto$	pip install django		

	-----------teste--------------
		python
		>>> import django
		>>> django.VERSION

	Crie um servidor 
	(OBS: o espaço ponto “ .” diz para criar na pasta atual)

	(venv) robson@robson:~/Documentos/pasta_do_projeto$
		django-admin startproject controle_gastos .


Criar a aplicação -------------------------------------------------------------------------------
	(venv) robson@robson:~/Documentos/pasta_do_projeto$
		python manage.py startapp contas

Cria o banco de dados em sqlLite-----------------------------------------------------------------
	(venv) robson@robson:~/Documentos/pasta_do_projeto$
		python manage.py migrate

Cria um super usuário ---------------------------------------------------------------------------
	(venv) robson@robson:~/Documentos/pasta_do_projeto$
		python manage.py createsuperuser

Faz o servidor rodar ----------------------------------------------------------------------------
	(venv) robson@robson:~/Documentos/pasta_do_projeto$
		python manage.py runserver
