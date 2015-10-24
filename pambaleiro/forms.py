# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from pambaleiro.models import Pambaleiro
import logging


class RegistrationForm(ModelForm):
    username = forms.CharField(label=u'Nick')
    first_name = forms.CharField(label=u'Nome')
    last_name = forms.CharField(label=u'Sobrenome')
    email = forms.EmailField(label=(u'Email'))
    password = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Confirme a sua password'),widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Pambaleiro
        exclude = ('user',)
        fields = ['first_name','last_name','username',
                  'email','password','password1','birth_date',
                  'country','city',]

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Este usuario ja existe, por favor escolha outro")

    def clean(self):
            if self.cleaned_data['password'] != self.cleaned_data['password1']:
                raise forms.ValidationError("Passwords diferentes, por favor tente de novo")
            return self.cleaned_data
