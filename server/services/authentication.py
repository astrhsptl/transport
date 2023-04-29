from abc import ABC, abstractclassmethod

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from authsystem.models import User


class BaseUserAuthentication(ABC):
    def __init__(self, request, serializer, **kwargs) -> None:
        self.request = request
        self.serializer = serializer

    @abstractclassmethod
    def authentication():
        pass

    @abstractclassmethod
    def register():
        pass 

class UserAuthentication:
    def __init__(self, request, serializer, presentaiton_serializer=None, **kwargs) -> None:

        self.request = request
        self.serializer = serializer
        self.presentaiton_serializer = presentaiton_serializer 
        
    def authentication(self,):
        from django.contrib.auth import authenticate

        user = authenticate(self.request,)

        if user:
            return self._serialize_user(user, self.presentaiton_serializer)

        return {'detail': 'authentication error'}, status.HTTP_400_BAD_REQUEST

    def register(self,):
        data = self.serializer(data=self.request.data)
        if data.is_valid():
            user = data.save()
            return self._serialize_user(user, self.presentaiton_serializer)

        return data.errors, status.HTTP_400_BAD_REQUEST
    

    def _get_tokens_for_user(self, user) -> dict:
        '''Get django user object. Return access and refresh tokens'''
        tokens = RefreshToken.for_user(user)
        return {
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }
    
    def _serialize_user(self, user, serializer):
        return {**dict(serializer(user).data), **self._get_tokens_for_user(user)}, status.HTTP_200_OK