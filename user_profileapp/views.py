# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponseRedirect, render_to_response, RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required



class UserRedirect(View):
    def get(self, request):
        #Todo mundo será redirecionado para o seu respectivo perfil
        return HttpResponseRedirect('/user/'+request.user.username)

class Profile(View):
    def get(self, request, username):
        params = dict()
        userProfile = Usuario.objects.get(username=username)
        params["profile"] = userProfile
        return render(request, 'base2.html', params)



class Index(View):
    def get(self,request):
        if request.user.is_authenticated():
            return render(request,'base2.html',{})
        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(request))

class Perfil(View):
    #@method_decorator(login_required)
    def get(self,request):
        print str(dir(request))
        #return render(request,'base2.html',{'usuario':'nome_de_teste'})
        return render(request,'profile.html',{'usuario':'nome_de_teste'})

class Login(View):
    def get(self,request):
        if request.user.is_authenticated():
            #return HttpResponseRedirect('/perfil/')
            print 'autenticado'
            return render_to_response('base2.html', {}, context_instance=RequestContext(request))

        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(request))
            #return render(request,'login.html',{})

    def post(self,request):
        msg_conta_desativada = 'Conta suspensa!'
        msg_dado_invalido = 'Dados invalidos!'
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        usuario_autenticado = authenticate(username=usuario,password=senha)

        if usuario_autenticado is not None:
            if usuario_autenticado.is_active:
                login(request, usuario_autenticado)
                contexto = {'usuario':usuario}
                #Retorna a pagina de perfil
                return render(request,'base2.html',contexto)
                #return HttpResponseRedirect('/perfil')
            else:
                contexto = {'msg':msg_conta_desativada}
                return render_to_response('login.html',contexto,context_instance=RequestContext(request))
        else:
            contexto = {'msg':msg_dado_invalido}
            return render_to_response('login.html',contexto,context_instance=RequestContext(request))

class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/login/')