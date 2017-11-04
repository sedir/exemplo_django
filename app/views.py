# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.decorators.csrf import csrf_exempt

from .forms import FuncionarioForm
from .models import Setor, Funcionario


# Create your views here.
# @csrf_exempt
# def hello_world(request):
#     if request.method=='GET':
#         return HttpResponse('ola mundo GET')
#     elif request.method=='POST':
#         return HttpResponse('ola mundo POST')
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class HelloWorldView(View):
#     def get(self, request):
#         return HttpResponse('ola mundo GET')
#
#     def post(self, request):
#         return HttpResponse('ola mundo POST')
#

class SetorList(ListView):
    model = Setor
    context_object_name = 'setores'
    template_name = 'app/setores.html'


class SetorCreate(SuccessMessageMixin, CreateView):
    model = Setor
    fields = ['nome']
    template_name = 'app/novo_setor.html'
    success_url = '/setores'
    success_message = 'O setor foi cadastrado com sucesso'


class FuncionarioCreate(SuccessMessageMixin, CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    # fields = ['nome', 'setor']
    template_name = 'app/novo_funcionario.html'
    success_url = '/setores'

    success_message = 'O funcionário foi cadastrado com sucesso'

