from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers import RegisterSerializer, LoginSerializer, UserSerializer
from app.utils import create_jwt_token


class RegisterEndpoint(CreateAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = create_jwt_token(user)
        user_data = UserSerializer(user).data

        return Response({
            'token': token,
            'user': user_data,
        }, status=status.HTTP_201_CREATED)


class LoginEndpoint(CreateAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token = create_jwt_token(user)
        user_data = UserSerializer(user).data

        return Response({
            'token': token,
            'user': user_data,
        }, status=status.HTTP_200_OK)
