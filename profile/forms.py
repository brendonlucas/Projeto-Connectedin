from django import forms


class FindUserForm(forms.Form):
    name_user = forms.CharField(max_length=255, required=True)
