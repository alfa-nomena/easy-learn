from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsOwnerOrReadOnly

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]