from django.shortcuts import render

from profile.forms import FindUserForm
from profile.models import Invite
from django.shortcuts import redirect
from authentication.models import User
from posts.forms import PostForm
from posts.models import Post
from django.core.paginator import Paginator


def index(request):
    profiles = User.objects.all()
    posts = Post.objects.filter(user=current_user(request))
    paginador = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginador.get_page(page)
    src = {'current_user': current_user(request), 'profiles': profiles, 'form': PostForm(), 'posts': posts}

    return render(request, 'index.html', src)


def show(request, profile_id):
    profile = User.objects.get(id=profile_id)
    args = {'profile': profile, 'current_user': current_user(request)}
    return render(request, 'profile.html', args)


def invite_friendship(request, profile_id):
    recipient = User.objects.get(id=profile_id)
    current_user(request).send_invite(recipient)
    return redirect('index')


def accept_friendship(request, invite_id):
    invite = Invite.objects.get(id=invite_id)
    invite.accept()
    invite.save()
    return redirect('index')


def refuse_friendship(request, invite_id):
    invite = Invite.objects.get(id=invite_id)
    invite.status = 2
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
                       'user_logado': current_user(request),
                       'ja_eh_contato': ja_eh_contato})
    else:
        return render(request, 'profile.html',
                      {'profile': profile, 'profile_logado': current_user(request),
                       'e_seu_profile': e_seu_profile})


def current_user(request):
    return request.user


def find_user(request):
    if request.method == 'POST':
        form = FindUserForm(request.POST)
        dados = form.data
        name = dados['name_user']
        print(name)
        users = User.objects.filter(first_name=name)
        return render(request, 'find_user.html', {'users': users, 'current_user': current_user(request)})
