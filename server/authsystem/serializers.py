from rest_framework import serializers

from .models import User


class LoginSerializer(serializers.ModelSerializer):
    '''Login serializer. Including name, surname, email, password, is_superuser, is_staff'''
    password = serializers.CharField(
        max_length=256
    )

    class Meta:
        model = User
        fields = ("email", 'password',)

class UserPresentationSerializer(serializers.ModelSerializer):
    '''Login serializer. Including name, surname, email, password, is_superuser, is_staff'''
    id = serializers.UUIDField()
    password = serializers.CharField(
        max_length=256
    )
    class Meta:
        model = User
        fields = ("__all__")
    
class UserRegisterSerializer(serializers.ModelSerializer):
    '''Register serializer. Including name, surname, email, password, is_superuser, is_staff'''
    password = serializers.CharField(
        max_length=256
    )
    class Meta:
        model = User
        fields = ("__all__")
    
    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data,)