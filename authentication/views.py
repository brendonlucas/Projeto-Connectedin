from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
import django.contrib.auth.views as djangoAuthViews



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
            usuario = User.objects.create_user(username=dados_form['username'], 
                                                email=dados_form['email'], 
                                                password=dados_form['password'], 
                                                first_name=dados_form['first_name'], 
                                                last_name=dados_form['last_name'])

            # usuario_dados = Perfil(telefone=dados_form['telefone'], nome_empresa=dados_form['nome_empresa'],
            #                        user=usuario)

            # usuario_dados.save()
            return redirect('signin')
        return render(request, self.template_name, {'form': form})

class LoginUserView(djangoAuthViews.LoginView):
    template_name = 'login.html'
    form = AuthenticationForm()

    def get(self, request):
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        return super(LoginUserView, self).post(request)