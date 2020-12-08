import jwt
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from MainExpensis import settings
from authentication.utils import generate_access_token, generate_refresh_token
from users.serializers import UserSerializerGet


class Authentication(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        User = get_user_model()
        email = request.data.get('email')
        password = request.data.get('password')
        response = Response()
        if (email is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'username and password required')

        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('wrong password')

        serialized_user = UserSerializerGet(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user, 1.0)

        response.data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': serialized_user,
        }

        return response


class RefreshToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        '''
        To obtain a new access_token this view expects 2 important things:
            1. a cookie that contains a valid refresh_token
            2. a header 'X-CSRFTOKEN' with a valid csrf token, client app can get it from cookies "csrftoken"
        '''
        User = get_user_model()
        refresh_token = request.COOKIES.get('refreshtoken')
        if refresh_token is None:
            raise exceptions.AuthenticationFailed(
                'Authentication credentials were not provided.')
        try:
            payload = jwt.decode(
                refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'expired refresh token, please login again.')

        user = User.objects.filter(id=payload.get('user_id')).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')

        access_token = generate_access_token(user)
        return Response({'access_token': access_token})
