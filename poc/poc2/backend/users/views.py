import email
from multiprocessing.reduction import send_handle
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Username em uso')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('usuário cadastrado')



def login_site(request):
    if request.method=='GET':
        return render(request, 'user_login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('email ou senha invalidos')


def logout_site(request):
    logout(request)
    return redirect('/')
    