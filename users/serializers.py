from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'gender',
            'birth_date',
            'monthly_limit',
            'income_scope'
        ]

    def hash_password(self):
        password = self.validated_data['password']
        self.validated_data['password'] = make_password(password)
