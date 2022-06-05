import email
from multiprocessing.reduction import send_handle
from sys import api_version
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import UserSerializer

#from .models import User
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

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
    



#ERRO (BAD REQUEST)
class AccountLoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({'login', 'login com sucesso'}, status=status.HTTP_200_OK)
            return Response({'Falha': 'credenciais invalidas'}, status=status.HTTP_200_OK)
        return Response({'error': 'Falha'}, status=status.HTTP_400_BAD_REQUEST)
#ERRO (BAD REQUEST)


#OK - FUNCIONAL
class AccountCreateView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            queryset = User.objects.filter(email=email)
            if(queryset.exists()):
                return Response({'Falha': 'Email em uso'}, status=status.HTTP_200_OK)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return Response({'created', 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)
        return Response({'Bad request': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)