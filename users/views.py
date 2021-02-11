from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializerPost, UserSerializerGet, UserSerializerPut
from users.service import get_user_by_id, get_user_by_auth_header


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

    """ update user """

    def put(self, request):
        user = get_user_by_auth_header(request.headers.get('Authorization'))
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = get_user_by_id(user.id)
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

    """ get user details """

    def get(self, request):
        user = get_user_by_auth_header(request.headers.get('Authorization'))
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = get_user_by_id(user.id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializerGet(user)
        return Response(serializer.data)
