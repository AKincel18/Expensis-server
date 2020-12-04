from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializerBase, UserSerializerIdNoPassword, UserSerializerNoPassword
from users.service import get_user_by_id


# path: /users/
class SaveUser(APIView):
    """ create user """

    def post(self, request):
        serializer = UserSerializerBase(data=request.data)
        if serializer.is_valid():
            serializer.hash_password()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# path: /users/<id>
class UserDetail(APIView):
    """ get user by id """

    def get(self, request, user_id):
        serializer = UserSerializerIdNoPassword(get_user_by_id(user_id))
        return Response(serializer.data)

    """ update user """

    def put(self, request, user_id):
        serializer = UserSerializerBase(get_user_by_id(user_id), data=request.data)
        if serializer.is_valid():
            serializer.hash_password()
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = UserSerializerNoPassword(get_user_by_id(user_id), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """delete user"""

    def delete(self, request, user_id):
        get_user_by_id(user_id).delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
