from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'gender',
            'birth_date',
            'monthly_limit',
            'income_range',
            'username'
        ]

    def hash_password(self):
        password = self.validated_data['password']
        self.validated_data['password'] = make_password(password)


class UserSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'gender',
            'birth_date',
            'monthly_limit',
            'income_range'
        ]


class UserSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'gender',
            'birth_date',
            'monthly_limit',
            'income_range'
        ]
