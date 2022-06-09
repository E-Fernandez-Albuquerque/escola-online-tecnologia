from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import UserSerializer

#from .models import User
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
#from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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