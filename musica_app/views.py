from django.shortcuts import render, HttpResponseRedirect, render_to_response, RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import View
from pambaleiro.models import Pambaleiro
from musica_app.models import Musica
from models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required




class MusicaView(View):
    @method_decorator(login_required)
    def get(self, request):
        params = dict()
        id = int(request.GET["id"])
        musica = Musica.objects.get(id=id)
        musicas = Musica.objects.all()
        params["musica"] = musica
        params["musicas"] = musicas
        return render(request,'musica.html', params)
