from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from app.utils import get_user_role


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        return get_user_role(obj)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'role')
