# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponseRedirect, render_to_response, RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import View
from pambaleiro.models import Pambaleiro
from musica_app.models import Musica, Gravacao, Comentario, Like
from models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required



class UserRedirect(View):
    def get(self, request):
        #Todo mundo será redirecionado para o seu respectivo perfil
        return HttpResponseRedirect('/user/'+request.user.username)


class Feed(View):
    @method_decorator(login_required)
    def get(self, request):
        params = dict()
        params['musicas'] = get_all_musics()
        params['gravacoes'] = get_all_shared_records()

        return render(request,'feed.html', params)

    def post(self, request):
        params = dict()
        params['musicas'] = get_all_musics()
        params['gravacoes'] = get_all_shared_records()

        #flag, 0 = comentario, 1 = like
        flag = int(request.POST["flag"])
        id = request.POST["id"]
        usuario = request.user.username
        print 'flag ',flag

        if flag == 0:
            comentario = request.POST["comentario"]
            gravacao = Gravacao.objects.filter(id=int(id))
            user = User.objects.filter(username=usuario)
            print user[0]
            print gravacao[0]
            comentario = Comentario.objects.create(texto=comentario,usuario=user[0],gravacao=gravacao[0])
            comentario.save()
            print "comentario salvo"

        elif flag == 1:
            print 'e1'
            gravacao = Gravacao.objects.filter(id=int(id))
            user = User.objects.filter(username=usuario)
            print user[0]
            print gravacao[0]
            like = Like.objects.create(usuario=user[0],gravacao=gravacao[0])
            like.save()
            print "like salvo"


        return render(request,'feed.html', params)

class MinhasGravacoes(View):
    @method_decorator(login_required)
    def get(self, request):
        params = dict()
        params['musicas'] = get_all_musics()
        params['gravacoes'] = get_all_shared_records_from(request.user.username)

        return render(request,'mgrav.html', params)





class Index(View):
    @method_decorator(login_required)
    def get(self,request):
        if request.user.is_authenticated():
            params = dict()
            params["musicas"] = get_all_musics()
            params["gravacoes"] = get_all_shared_records_from(request.user.username)
            return render(request,'feed.html',params)
        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(request))

class Perfil(View):
    @method_decorator(login_required)
    def get(self,request):
        params = dict()
        username = str(request.user.username)
        user = User.objects.get(username=username)


        pamb = get_pambaleiro_from(user)
        params["pambaleiro"] = pamb
        params["musicas"] = get_all_musics()
        return render(request,'profile.html',params)


class MembrosView(View):
    @method_decorator(login_required)
    def get(self, request):
        params = dict()
        username = str(request.user.username)
        user = User.objects.get(username=username)
        params["membros"]=  get_all_users()
        params["musicas"] = get_all_musics()
        return render(request,'members.html',params)




class Login(View):
    def get(self,request):
        if request.user.is_authenticated():
            #return HttpResponseRedirect('/perfil/')
            params = dict()
            musicas = Musica.objects.all()
            params["musicas"] = musicas
            print 'autenticado'
            musicas  = Musica.objects.all()
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


def get_all_pambaleiros():
    return Pambaleiro.objects.all()

def get_all_users():
    return User.objects.all()


def get_all_musics():
    return Musica.objects.all()

def get_all_records():
    return Gravacao.objects.all()

def get_all_comments():
    return Comentario.objects.all()

def get_user_from(username):
    return User.objects.get(username=username)

def get_pambaleiro_from(user):
    return Pambaleiro.objects.get(user=user)

def get_all_shared_records():
    return Gravacao.objects.filter(compartilhada=True)

def get_all_records_from(username):
    user = User.objects.get(username=username)
    print Gravacao.objects.filter(usuario=user)


def get_all_shared_records_from(username):
    user = User.objects.get(username=username)
    return Gravacao.objects.filter(usuario=user,compartilhada=True)

def get_all_comments_from(id):
    return Comentario.objects.filter(id=id)

