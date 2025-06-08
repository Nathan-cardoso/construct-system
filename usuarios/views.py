from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('cadastrar_vendedores')
def cadastrar_vendedor(request):
    return HttpResponse('teste')
