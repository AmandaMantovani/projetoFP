from django.shortcuts import render, HttpResponseRedirect
from caixas.models import Caixa

def index(request):
	return render(request,'index.html')
	
def caixaListar(request):
    caixas = Caixa.objects.all()[0:10] # isto e o select no banco lista os dez primeiros registros encontrados
    # TESTE LOCAL PARA VERIFICAR SE A TABELA ESTA LISTANDO
    #pessoas = []
    #pessoas.append(Pessoa(nome='UNIFRAN', email='MAIL'))
    #pessoas.append(Pessoa(nome='CRUZEIRO'))
    return render(request, 'caixas/listaCaixas.html', {'caixas': caixas})

def caixaAdicionar(request):
    return render(request, 'caixas/formCaixas.html')

def caixaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')
        # 'codigo' e o nome do text no formpessoas

        try:
            caixa = Caixa.objects.get(pk=codigo)
        except:
            caixa = Caixa()

        caixa.tipo = request.POST.get('tipo', '')
        caixa.descricao = request.POST.get('descricao', '')
        caixa.valor = request.POST.get('valor', '')
        caixa.pagseguro = request.POST.get('pagseguro', '')
        caixa.data = request.POST.get('data', '00/00/0000')

        caixa.save()
        return HttpResponseRedirect('/caixas/pesquisar/')
        # a primeira barra evita a mudanca do html pois caracteriza iniciar

def caixaPesquisar(request):

    texto = request.POST.get('textoBusca', '')

    print '=====>'+texto

    caixas = Caixa.objects.filter(descricao__contains=texto)

    return render(request, 'caixas/listaCaixas.html', {'caixas': caixas})