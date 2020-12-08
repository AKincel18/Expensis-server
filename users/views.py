from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions

from users.serializers import UserSerializerPost, UserSerializerGet, UserSerializerPut
from users.service import get_user_by_id


# path: /users/
class SaveUser(APIView):
    """ create user """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.hash_password()
            save_response = serializer.save()
            return Response(UserSerializerGet(save_response).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# path: /users/<id>
class UserDetail(APIView):
    """ get user by id """

    def get(self, request, user_id):
        user = get_user_by_id(user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializerGet(user)
        return Response(serializer.data)

    """ update user """

    def put(self, request, user_id):
        user = get_user_by_id(user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializerPost(user, data=request.data)
        if serializer.is_valid():
            serializer.hash_password()
            save_response = serializer.save()
            return Response(UserSerializerGet(save_response).data)
        else:
            serializer = UserSerializerPut(user, data=request.data)
            if serializer.is_valid():
                save_response = serializer.save()
                return Response(UserSerializerGet(save_response).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """delete user"""

    def delete(self, request, user_id):
        user = get_user_by_id(user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
