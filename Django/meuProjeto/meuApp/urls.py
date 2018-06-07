# arquivo de urls do meuApp
# ajuda a nao sobrecarregar o urls.py do servidor 

from django.urls import path
from .views import retornarHtmlCom, retornarInformacaoComDados, create, read, update, delete

#   	1° url			2° view				3° link
urlpatterns = [
    path('home/',		retornarHtmlCom),
    path('artigos/<int:year>/',	retornarInformacaoComDados),
    path('ler/',		read, 				name='url_ler'),
    path('criar/',		create, 			name='url_criar'),
    path('atualizar/<int:pk>/',	update, 			name='url_atualizar'),
    path('deletar/<int:pk>/',	delete, 			name='url_deletar'),
]
