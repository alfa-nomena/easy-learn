from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" # ['id', 'username', 'name', 'email', 'is_staff', 'is_active', 'date_joined',]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }