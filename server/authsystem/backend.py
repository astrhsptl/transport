import jwt

from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.backends import BaseBackend
from rest_framework.authentication import (
    get_authorization_header
)

from authsystem.models import User

class JWTAuthClass(BaseBackend):
    def authenticate(self, request):
        headers = get_authorization_header(request)
        email = request.data.get('email')
        username = request.data.get('username')

        if headers:
            return self._auth_by_jwt(headers)
        elif email:
            password = request.data.get('password')
            return self._auth_by_email(email, password) 
        elif username:
            password = request.data.get('password')
            return self._auth_by_username(username, password) 

        return None

    def _auth_by_jwt(self, headers):
        auth_data = headers.decode('utf-8')
        auth_token = auth_data.split(' ')

        if len(auth_token) != 2:
            return None

        token = auth_token[1]

        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, 'HS256')
            user = User.objects.get(pk=decoded['user_id'])
            return user
        except:
            return None

    def _auth_by_email(self, email, password):
        try:
            user = User.objects.get(email=email)
        except:
            return None
        
        if user.check_password(password):
            return user
        
        return None
    
    def _auth_by_username(self, username, password):
        try:
            user = User.objects.get(username=username)
        except:
            return None
        
        if user.check_password(password):
            return user
        
        return None