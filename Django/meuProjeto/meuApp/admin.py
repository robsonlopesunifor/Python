# E possivel passar os modol para o admin
# Assim voce pode adicionar, remover, e editar os models

from django.contrib import admin

# 1° voce importa os models
from .models import Categoria	
from .models import Transacao

# 2° voce adiciona os models ao registro do admin
admin.site.register(Categoria)
admin.site.register(Transacao)

