# -*- encoding:utf-8 -*-

from django.forms import ModelForm
from django import forms
from principal.models import Post, Comentario

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class PostForm(ModelForm):
    class Meta:
        model = Post

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario