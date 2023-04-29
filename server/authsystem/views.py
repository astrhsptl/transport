from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate

from services.authentication import UserAuthentication

from .models import User
from .serializers import UserPresentationSerializer, LoginSerializer, UserRegisterSerializer

class LoginAPIView(generics.GenericAPIView):
    '''This api relise sign in on jwt architecture. Return name, surname, email, is_superuser, is_staff and access token. Supports only post request'''
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )
    presentation_serializer = UserPresentationSerializer
    
    def post(self, request) -> Response:
        authentication = UserAuthentication(request, self.serializer_class, self.presentation_serializer)
        return Response(*authentication.authentication())

class RegisterAPIView(generics.GenericAPIView):
    '''This api relise sign up on jwt architecture. Return  name, surname, email, is_superuser, is_staff '''
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny, )
    presentation_serializer = UserPresentationSerializer

    def post(self, request) -> Response:
        authentication = UserAuthentication(request, self.serializer_class, self.presentation_serializer)
        return Response(*authentication.register())