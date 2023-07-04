from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return Comment.objects.filter(course=self.kwargs['course_id'])