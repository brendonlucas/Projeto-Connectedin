from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all(),
                                          'perfil_logado': get_perfil_logado(request)})


def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html',
                  {'perfil': perfil,
                   'perfil_logado': get_perfil_logado(request)})


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id=2)


def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    e_seu_perfil = perfil_logado.id == perfil_id
    if not e_seu_perfil:
        return render(request, 'perfil.html',
                      {'perfil': perfil, 'perfil_logado': get_perfil_logado(request), 'ja_eh_contato': ja_eh_contato})
    else:
        return render(request, 'perfil.html',
                      {'perfil': perfil, 'perfil_logado': get_perfil_logado(request),
                       'e_seu_perfil': e_seu_perfil})


def login(request):
    return render(request, 'login.html')


def registrar(request):
    return render(request, 'registrar.html')
