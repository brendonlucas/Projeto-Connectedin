from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from profile.forms import FindUserForm
from profile.models import Invite
from django.shortcuts import redirect
from authentication.models import User, Convite
from posts.forms import PostForm, CommentForm
from posts.models import Post
from django.core.paginator import Paginator


@login_required
def index(request):
    profiles = User.objects.all()
    posts = Post.objects.filter(user=current_user(request), type_post='0')
    paginador = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginador.get_page(page)

    src = {'current_user': current_user(request), 'profiles': profiles, 'form': PostForm(),
           'comment_form': CommentForm(), 'posts': posts}

    return render(request, 'index.html', src)


def show(request, profile_id):
    profile = User.objects.get(id=profile_id)
    convites = Convite.objects.filter(solicitante=current_user(request).id)
    args = {'profile': profile, 'current_user': current_user(request), 'convites': convites}
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


@login_required
def set_admin(request, profile_id):
    profile = User.objects.get(id=profile_id)
    if profile.is_superuser:
        profile.is_superuser = False
        profile.save()
    else:
        profile.is_superuser = True
        profile.save()
    return redirect('show_user', profile_id)


@login_required
def find_user(request):
    if request.method == 'POST':
        form = FindUserForm(request.POST)
        dados = form.data
        name = dados['name_user']
        return redirect('find_user_link', name)
    else:
        return render(request, 'find_user.html', {'users': None, 'current_user': current_user(request)})


@login_required
def find_user_in_link(request, username):
    users = User.objects.filter(first_name=username)
    paginador = Paginator(users, 10)
    page = request.GET.get('page')
    users = paginador.get_page(page)
    return render(request, 'find_user.html', {'users': users, 'current_user': current_user(request)})


@login_required
def page_admin(request):
    if current_user(request).is_superuser:
        convites = Convite.objects.filter(solicitante=current_user(request).id)
        users = User.objects.all()
        paginador = Paginator(users, 10)
        page = request.GET.get('page')
        users = paginador.get_page(page)
        return render(request, 'pag_superuser.html', {'current_user': current_user(request), 'profiles': users,
                                                      'convites': convites})
    else:
        return render(request, 'access_denied.html', {'current_user': current_user(request)})


@login_required
def convidar(request, profile_id):
    perfil_a_convidar = User.objects.get(id=profile_id)
    perfil_logado = current_user(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


@login_required
def aceitar(request, invite_id):
    convite = Convite.objects.get(id=invite_id)
    convite.aceitar()
    return redirect('index')


@login_required
def recusar(request, invite_id):
    convite = Convite.objects.get(id=invite_id)
    convite.recusar()
    return redirect('index')


def desfazer(request, perfil_id):
    perfil = User.objects.get(id=perfil_id)
    current_user(request).friendship.filter()
    perfil.desfazer()
    return redirect('index')
