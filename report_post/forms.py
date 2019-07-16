from django import forms
from authentication.models import User


class FormReportPost(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, required=False)
