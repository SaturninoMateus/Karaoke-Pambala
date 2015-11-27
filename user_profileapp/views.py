# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponseRedirect, render_to_response, RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import View
from pambaleiro.models import Pambaleiro
from musica_app.models import Musica, Gravacao
from models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required



class UserRedirect(View):
    def get(self, request):
        #Todo mundo será redirecionado para o seu respectivo perfil
        return HttpResponseRedirect('/user/'+request.user.username)


class Profile(View):
    @method_decorator(login_required)
    def get(self, request, username):
        params = dict()
        userProfile = Usuario.objects.get(username=username)
        params["profile"] = userProfile
        return render(request, 'base2.html', params)


class Feed(View):
    @method_decorator(login_required)
    def get(self, request):
        musicas = Musica.objects.all()
        gravacoes = Gravacao.objects.all()
        print gravacoes
        params = dict()
        params['musicas'] = musicas
        return render(request,'feed.html', params)





class Index(View):
    @method_decorator(login_required)
    def get(self,request):
        if request.user.is_authenticated():
            params = dict()
            musicas = Musica.objects.all()
            gravacoes = Gravacao.objects.all()
            print gravacoes
            musicas = Musica.objects.all()
            params["musicas"] = musicas
            return render(request,'feed.html',params)
        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(request))

class Perfil(View):
    @method_decorator(login_required)
    def get(self,request):
        params = dict()
        username = str(request.user.username)
        musicas = Musica.objects.all()
        print 'username: ', username
        user = User.objects.get(username=username)
        pambaleiro = Pambaleiro.objects.get(user=user)
        params["pambaleiro"] = pambaleiro
        params["musicas"] = musicas

        #return render(request,'base2.html',{'usuario':'nome_de_teste'})
        print dir(pambaleiro)
        return render(request,'profile.html',params)


class MembrosView(View):
    @method_decorator(login_required)
    def get(self, request):
        username = str(request.user.username)
        user = User.objects.get(username=username)
        musicas = Musica.objects.all()
        params = dict()
        membros = User.objects.all()
        params["membros"]= membros
        params["musicas"] = musicas
        return render(request,'members.html',params)




class Login(View):
    def get(self,request):
        if request.user.is_authenticated():
            #return HttpResponseRedirect('/perfil/')
            params = dict()
            musicas = Musica.objects.all()
            params["musicas"] = musicas
            print 'autenticado'
            musicas = Musica.objects.all()
            return render_to_response('feed.html', params, context_instance=RequestContext(request))

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
                #Usuario autenticado, entao redireciana pra pagina de feed
                return render(request,'feed.html',contexto)
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