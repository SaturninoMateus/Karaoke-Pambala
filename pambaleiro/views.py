# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from pambaleiro.models import Pambaleiro

from django.template import RequestContext
from pambaleiro.forms import RegistrationForm


class PambaleiroRegistration(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/perfil/')
        else:
            '''User is not submitting the forms, show them a blank registration form'''
            form = RegistrationForm()
            context = {'form':form}
            return render_to_response('registration.html', context, context_instance=RequestContext(request))

    def post(self, request):
        form = RegistrationForm(request.POST)
        print '1'
        if form.is_valid():
            print 'criando usuario'
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email =form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],)

            user.save()
            print 'criado com  sucesso'
            #pambaleiro = user.get_profile() #Foi retirado a partir do django 1.7
            pambaleiro = Pambaleiro(user=user, birth_date=form.cleaned_data['birth_date'],
                                    country=form.cleaned_data['country'], city=form.cleaned_data['city'])
            pambaleiro.name = form.cleaned_data['first_name']
            pambaleiro.birth_date  = form.cleaned_data['birth_date']
            pambaleiro.save()
            print 'pronto'
            return HttpResponseRedirect('/perfil/')
        else:
            form = RegistrationForm()
            context = {'form':form}
            print ':( entrou no else'
            return render_to_response('registration.html', context, context_instance=RequestContext(request))
