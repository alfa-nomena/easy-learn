from rest_framework import viewsets

from rates.models import Rate
from rates.serializers import RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    serializer_class = RateSerializer
    lookup_field = 'pk'
    
    
    def get_queryset(self):
        return Rate.objects.filter(course=self.kwargs['course_id'])