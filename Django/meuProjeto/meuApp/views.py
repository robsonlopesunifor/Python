# metodos chamados pelo arquivo urls.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm # voce tem que importar os form caso necessario
import datetime


def retornarHtmlCom(request):
    html = "<html><body>Pagina simples</body></html>"
    return HttpResponse(html)

def retornarInformacaoComDados(request, year):
    return HttpResponse('Passando valor da url: url/year/ ' + str(year)) # voce pode enviar qualquer coisa

def retornarTeplateComDados(request):
    return render(request, 'home.html', data) # e possivel adicionar dados ao template


def read(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    # retorna todos
    # Transacao é o model (from .models import Transacao)
    # o objects e o manega que contem os comandos sql que interage com banco de dados
    return render(request, 'listagem.html', data)


def create(request):
    data = {}
    form = TransacaoForm(request.POST,request.FILES, None)
    # TransacaoForm e a class do arquivo .form que herda ModelForm (from .form import TransacaoForm)
    # caso tiver dados enviados via POST passe para o form
    # caso tiver arquivo passe para o form
    # caso contrario passe nada para o form

    if form.is_valid(): # se o formulario for valido
        form.save()     # como ele tambem contem o model, e possivel usar .save()
        return redirect('url_ler')

    return render(request, 'form.html', {'form': form})


def update(request, pk):
    data = {}
    #---------------------------------------------------------------
    transacao = Transacao.objects.get(pk=pk)
    # filtra a instacia do model pela chave
    # Transacao é o model (from .models import Transacao)
    # o objects e o manega que contem os comandos sql que interage com banco de dados

    form = TransacaoForm(request.POST or None, instance=transacao)
    # preenche o form com a instacia do model (transacao)

    if form.is_valid(): # se for valido
        form.save() # salvar a auteracao
        return redirect('url_ler')  # listagem(request)

    data['form'] = form           # coloca em um dicionario para acessar no template
    data['transacao'] = transacao # coloca em um dicionario para acessar no template
    return render(request, 'form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    # filtra a instacia do model pela chave
    transacao.delete()
    # deleta a instacia do model
    return redirect('url_ler')


