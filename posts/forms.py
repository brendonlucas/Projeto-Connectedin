from django.core.exceptions import ValidationError
from django import forms
from .models import Post


class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    content = forms.CharField(widget=forms.Textarea, required=False)

    #def is_valid(self):
    #    if image is None or content is None:
    #        raise ValidationError('A postagem requer um texto e/ou uma imagem', code='post_error')
