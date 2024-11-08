from django.shortcuts import render

# Create your views here.


# authapp/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, email=email, password=password)
    UserProfile.objects.create(user=user)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            'avatar': request.build_absolute_uri(user_profile.avatar.url) if user_profile.avatar else None,
            'status': user_profile.status,
            'score': user_profile.score
        }, status=status.HTTP_200_OK)
    return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
