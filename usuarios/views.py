from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth

@has_permission_decorator('cadastrar_vendedores')
def cadastrar_vendedor(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_vendedor.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)

        if user.exists():
            return HttpResponse('Usuário já cadastrado')
        
        user = Users.objects.create_user(
            username=email,
            email=email,
            password=senha,
            cargo="V"
        )

        return HttpResponse('Usuário cadastrado com sucesso')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('home'))  # Redireciona para a página inicial se já estiver logado
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            return HttpResponse('Usuário ou senha inválidos')
        
        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')


def logout(request):
    request.session.flush()  # Limpa a sessão do usuário
    return redirect(reverse('login'))  # Redireciona para a página de login