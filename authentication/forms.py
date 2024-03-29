from profile.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


class UserRegisterForm(forms.Form):
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'border rounded', 'style': 'width: 150px;height: 150px;object-fit: cover;'}))
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def is_valid(self):
        valid = True
        if not super(UserRegisterForm, self).is_valid():
            self.add_erro(_('Por favor, verifique os dados informados'))
            valid = False

        user_exists = User.objects.filter(username=self.cleaned_data['username']).exists()
        if user_exists:
            self.add_erro(_('Usuário já existente.'))
            valid = False

        email_exists = User.objects.filter(email=self.cleaned_data['email']).exists()
        if email_exists:
            self.add_erro(_('Email já cadastrado.'))
            valid = False
        return valid

    def add_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
