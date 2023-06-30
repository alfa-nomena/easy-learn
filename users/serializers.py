from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'is_superuser',
            'date_joined',
            'password',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }