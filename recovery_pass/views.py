from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.views.generic.base import View
from authentication.models import User
from django.core.mail import send_mail
from recovery_pass.models import Send
from django.contrib import messages
from recovery_pass.forms import *
from datetime import date
import random


def get_current_user(request):
    return request.user


def recovery_password(request, link):
    form = ChangePassForm()
    try:
        link_exists = Send.objects.get(body_link=link)
        data_atual = date.today()
        if link_exists is not None:
            if link_exists.active == 1:
                if data_atual == link_exists.date_link:
                    if request.method == 'POST':
                        form = ChangePassForm(request.POST)
                        if form.is_valid():
                            dados = form.data
                            new_password = dados['new_pass']
                            user = User.objects.get(email=link_exists.user_link.email)
                            hashed_pwd = make_password(new_password)
                            user.password = hashed_pwd
                            user.save()

                            link_exists.active = 0
                            link_exists.save()
                            return redirect('signin')
                    elif request.method == 'GET':
                        return render(request, 'pag_redefine_password.html', {'form': form})
                else:
                    link_exists.active = 0
                    link_exists.save()
                    return render(request, 'pag_link_has_expired.html')
            else:
                return render(request, 'pag_link_has_expired.html')
        else:
            return render(request, 'pag_link_has_expired.html')
    except Send.DoesNotExist:
        return render(request, 'pag_link_has_expired.html')
    return render(request, 'pag_redefine_password.html', {'form': form})


def gerar_link(email_user):
    while True:
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'h']
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        link = ''
        for x in range(7):
            num_letra = random.randint(0, 10)
            link += letras[num_letra]

        for i in range(6):
            num_letra = random.randint(0, 9)
            link += str(numeros[num_letra])
        try:
            link_exists = Send.objects.get(body_link=link)

        except Send.DoesNotExist:
            user = User.objects.get(email__exact=email_user)
            Send(body_link=link, active=1, user_link=user).save()
            break
    return link


class SendEmailView(View):
    template_name = 'pag_recovery.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print('post')
        form = SendEmailForm(request.POST)
        if form.is_valid():
            print('valido')
            dados_form = form.cleaned_data
            email_user = dados_form['email']
            link_gerado = gerar_link(email_user)
            mensagem = 'Link para recuperar senha do connectedin \n' + 'http://127.0.0.1:8000/recuperar-senha/' + \
                       link_gerado
            send_mail('Email para recuperacao', mensagem, 'projectconnectedin@gmail.com',
                      [email_user]
                      , fail_silently=False)
            return redirect('signin')
        return render(request, self.template_name, {'form': form})


@login_required
def change_password(request):
    form = ChangePassUserForm()
    if request.method == 'POST':
        form = ChangePassUserForm(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            old_pass = dados['current_pass']
            new_pass = dados['new_pass']
            pass_valid = get_current_user(request).check_password(old_pass)
            if pass_valid:
                user = get_current_user(request)
                hashed_pwd = make_password(new_pass)
                user.password = hashed_pwd
                user.save()
                return redirect('signin')
            else:
                messages.error(request, 'A Senha informada não confere com sua conta!')
                return redirect('change_pass')

    elif request.method == 'GET':
        return render(request, 'pag_change_password.html',
                      {'form': form, 'current_user': get_current_user(request)})
    else:
        return render(request, 'pag_change_password.html', {'current_user': get_current_user(request)})
