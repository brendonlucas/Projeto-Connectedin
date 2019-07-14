from django import forms
from .models import Post


class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    content = forms.CharField(widget=forms.Textarea, required=False)

    def is_valid(self):
        valid = super(PostForm, self).is_valid()
        image = self.cleaned_data.get('image')
        content = self.cleaned_data.get('content')

        if image is None and content == '':
            self.add_error('Seu post precisa de um texto e/ou uma imagem')
            valid = False

        return valid

    def add_error(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
        
class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=False)

    def is_valid(self):
        valid = super(CommentForm, self).is_valid()
        content = self.cleaned_data.get('content')

        if content == '':
            self.add_error('Seu comentário precisa de um conteúdo')
        
        return valid

    def add_error(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)