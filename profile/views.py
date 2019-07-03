from django.shortcuts import render
from profile.models import Invite
from django.shortcuts import redirect
from authentication.models import User

def index(request):
    current_user = current_user(request)
    src = {'current_user': current_user }
    return render(request, 'index.html', src )


def show(request, profile_id):
    profile = User.objects.get(id=profile_id)
    args = {'profile': profile, 'current_user': current_user(request)}
    return render(request, 'profile.html', args)


def invite_user(request, profile_id):
    recipient = User.objects.get(id=profile_id)
    current_user(request).send_invite(recipient)
    return redirect('index')

def accept_invite(request, convite_id):
    invite = Invite.objects.get(id=convite_id)
    invite.accept()
    invite.save()
    return redirect('index')


def exibir(request, profile_id):
    profile = User.objects.get(id=profile_id)
    profile_logado = current_user(request)
    ja_eh_contato = profile in profile_logado.contatos.all()
    e_seu_profile = profile_logado.id == profile_id
    print(ja_eh_contato)
    if not e_seu_profile:
        return render(request, 'profile.html',
                      {'profile': profile, 'profile_logado': current_user(request),
                       'user_logado': get_user_logado(request),
                       'ja_eh_contato': ja_eh_contato})
    else:
        return render(request, 'profile.html',
                      {'profile': profile, 'profile_logado': current_user(request),
                       'e_seu_profile': e_seu_profile})

def current_user(request):
    return request.user