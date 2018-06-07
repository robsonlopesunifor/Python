# cria formularios altomaticos com base em um model 

# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
from django.forms import ModelForm # cria formularios altomaticos
from .models import Transacao      # importa os models para gerar os campos

class TransacaoForm(ModelForm):
    class Meta:
	# model que voce quer
        model = Transacao
	# campos que voce quer
        fields = ['data','descricao','valor','observacoes','categoria','photo']
