from rest_framework import routers
from courses.views import CourseViewSet
from users.views import UserViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('courses', CourseViewSet)