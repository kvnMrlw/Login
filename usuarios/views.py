from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as log
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Esse nome já existe")

        user = User.objects.create_user(username=username, email=email, password=senha)
        

       
        return HttpResponse("usuário cadastrado com sucesso!")
        
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST": 
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            log(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Usuario ou senha incorreto!')

@login_required
def plataforma(request):
    return HttpResponse('Erro ao tentar logar')