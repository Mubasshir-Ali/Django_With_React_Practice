from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_framework.response import Response 
from django.http.response import Http404
from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .renderers import UserRenderer  
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
from .models import User
from django.contrib import messages
from datetime import date
from django.db.models import Q
from django.urls import reverse
# from .forms import OnlineAdmissionForms

from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model

# from . forms import UserRegisterForm
from django.views import View
from .models import UserManager


from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# from django.core.files.storage import default_storag
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.shortcuts import render,get_object_or_404

# from .models import *
# from .serializers import *


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        name = [user.name for user in User.objects.all()]
        return Response(name) 

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg': 'Login Success'}, 
        status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors':['Email or Password is not Valid']}}, 
        status=status.HTTP_404_NOT_FOUND)
                
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        # if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password Changed Successfully."})
        return Response(serializer.errors, status=400)
        
class SendPasswordResetEmailView(APIView):
    def post(self, request):
        serializer = SendPasswordResetEmailSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.send_reset_email()
            return Response({"detail": "Password reset email sent."})
        return Response(serializer.errors, status=400)
        
class UserPasswordResetView(APIView):
    def post(self, request):
        serializer = UserPasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password reset Successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)

########################################################################