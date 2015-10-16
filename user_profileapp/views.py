from django.shortcuts import render
from django.views.generic import View
from models import Usuario


class Index(View):
    def get(self, request):
        params = {}
        params['usuarios'] = Usuario.objects.all()
        return render(request,'index.html',params)
