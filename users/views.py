from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from .permissions import UserPermission


class UserViewSet(
        viewsets.ModelViewSet
    ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes=[
        UserPermission,
    ]