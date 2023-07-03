from rest_framework import serializers
from .models import User
from courses.serializers import CourseSerializer

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
            'course_set'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        depth=1
        
        