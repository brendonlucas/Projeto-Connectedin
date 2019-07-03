from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    

    def is_valid(self):
        valid = True
        if not super(UserRegisterForm, self).is_valid():
            self.add_error('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.cleaned_data['username']).exists()
        if user_exists:
            self.add_error('Usuário já existente.')
            valid = False
        return valid

    def add_error(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
