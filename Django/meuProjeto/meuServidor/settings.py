"""
Para mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/2.0/topics/settings/

Para obter a lista completa de configurações e seus valores, consulte
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# /////////////// Construir caminhos dentro do projeto como este: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# /////////////// SECURITY WARNING: não execute com depuração ativada na produção!
# /////////////// Use True para o modo desenvolvedor 
DEBUG = True


# /////////////// Defina seus apicativos aki
INSTALLED_APPS = [
    'meuApp',
]

# /////////////// Defina seus templates aki
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'contas/templates')],
    },
]

# /////////////// link para acessar os diretorios dos arquivos estaticos 
STATIC_URL = '/static/'

# /////////////// Diretorio dos arquivos estaticos 
STATICFILES_DIRS = [
    'contas/estaticos',
]

# /////////////// link para acessar os diretorios dos arquivos de media 
MEDIA_URL = '/media/'

# /////////////// Diretorio dos arquivos de media 
MEDIA_ROOT = 'contas/media'

