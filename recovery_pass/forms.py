from django import forms
from authentication.models import User


class SendEmailForm(forms.Form):
    email = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(SendEmailForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(email=self.cleaned_data['email']).exists()
        if not user_exists:
            self.adiciona_erro('Email solicitado não esta registrado.')
            valid = False
        return valid

    def adiciona_erro(self, message):

        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


class ChangePassForm(forms.Form):
    new_pass = forms.CharField(required=True)


class ChangePassUserForm(forms.Form):
    current_pass = forms.CharField(required=True)
    new_pass = forms.CharField(required=True)