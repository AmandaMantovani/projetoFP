from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa

def listarFluxos(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'fluxos/listarFluxos.html', {'pessoas': pessoas})

