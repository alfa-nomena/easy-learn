from rest_framework import routers
from comments.views import CommentViewSet
from courses.views import CourseViewSet
from rates.views import RateViewSet
from users.views import UserViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('courses', CourseViewSet)
router.register(r'courses/(?P<course_id>\d+)/comments', CommentViewSet, basename='comments')
router.register(r'courses/(?P<course_id>\d+)/rates', RateViewSet, basename='rates')