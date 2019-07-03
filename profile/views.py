from django.shortcuts import render
from profile.models import Perfil, Convite
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all(),
                                          'perfil_logado': get_perfil_logado(request),
                                          'user_logado': get_user_logado(request)})


def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html',
                  {'perfil': perfil,
                   'perfil_logado': get_perfil_logado(request), 'user_logado': get_user_logado(request)})


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    print(perfil_a_convidar.id)
    perfil_logado = get_perfil_logado(request)
    print(perfil_logado.id)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


def get_user_logado(request):
    return request.user


def get_perfil_logado(request):
    user_logado = get_user_logado(request)
    return Perfil.objects.get(user_id=user_logado.id)


def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    e_seu_perfil = perfil_logado.id == perfil_id
    print(ja_eh_contato)
    if not e_seu_perfil:
        return render(request, 'perfil.html',
                      {'perfil': perfil, 'perfil_logado': get_perfil_logado(request),
                       'user_logado': get_user_logado(request),
                       'ja_eh_contato': ja_eh_contato})
    else:
        return render(request, 'perfil.html',
                      {'perfil': perfil, 'perfil_logado': get_perfil_logado(request),
                       'e_seu_perfil': e_seu_perfil})
