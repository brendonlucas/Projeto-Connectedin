from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import *
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from profile.models import *
from authentication.forms import UserRegisterForm


# @method_decorator(login_required, name='dispatch')
class RegisterUserView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name, {'form': UserRegisterForm()})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            usuario = User.objects.create_user(username=dados_form['nome'], email=dados_form['email'],
                                               password=dados_form['senha'], first_name=dados_form['first_name'],
                                               last_name=dados_form['last_name'])

            usuario_dados = Perfil(telefone=dados_form['telefone'], nome_empresa=dados_form['nome_empresa'],
                                   user=usuario)

            usuario_dados.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})

