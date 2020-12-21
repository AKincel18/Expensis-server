from users.models import User
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions

from MainExpensis.error_messages import user_not_found_error, user_is_inactive_error, access_token_expired_error, \
    missing_token_prefix_error


def get_user_by_id(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None


def get_user_by_auth_header(authorization_header):
    if not authorization_header:
        return None
    try:
        # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
        access_token = authorization_header.split(' ')[1]
        payload = jwt.decode(
            access_token, settings.SECRET_KEY, algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(access_token_expired_error)
    except IndexError:
        raise exceptions.AuthenticationFailed(missing_token_prefix_error)

    user_model = get_user_model()
    user = user_model.objects.filter(id=payload['user_id']).first()

    if user is None:
        raise exceptions.AuthenticationFailed(user_not_found_error)

    if not user.is_active:
        raise exceptions.AuthenticationFailed(user_is_inactive_error)

    return user
