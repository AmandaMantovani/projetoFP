from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa

def index(request):
	return render(request,'index.html')
	
def pessoaListar(request):
    pessoas = Pessoa.objects.all()[0:10] # isto e o select no banco lista os dez primeiros registros encontrados
    # TESTE LOCAL PARA VERIFICAR SE A TABELA ESTA LISTANDO
    #pessoas = []
    #pessoas.append(Pessoa(nome='UNIFRAN', email='MAIL'))
    #pessoas.append(Pessoa(nome='CRUZEIRO'))
    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

def pessoaAdicionar(request):
    return render(request, 'pessoas/formPessoas.html')

def pessoaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')
        # 'codigo' e o nome do text no formpessoas

        try:
            pessoa = Pessoa.objects.get(pk=codigo)
        except:
            pessoa = Pessoa()

        pessoa.nome = request.POST.get('nome', '')
        pessoa.email = request.POST.get('email', '')
        pessoa.telefone = request.POST.get('telefone', '(00) 0-0000-0000')
        pessoa.logradouro = request.POST.get('logradouro', '')

        pessoa.save()
        return HttpResponseRedirect('/pessoas/')
        # a primeira barra evita a mudanca do html pois caracteriza iniciar

def pessoaPesquisar(request):

    texto = request.POST.get('textoBusca', '')

    print '=====>'+texto

    pessoas = Pessoa.objects.filter(nome__contains=texto)

    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})