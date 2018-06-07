"""
Funcao 
    1. from my_app import views
    2. path('', views.home, name='home')
Class
    1. from outro_app.views import nomeClasse
    2. path('', nomeClasse.metodo(), name='home')
URLconf
    1. from django.urls import include, path

    2. path('blog/', include('contas.urls'))

    2. from contas import urls as contas_urls
    3. path('blog/', include(contas_urls))
"""

from django.contrib import admin
from django.urls import path, include
from contas import urls as contas_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include(contas_urls)),
]
