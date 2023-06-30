from django.contrib import admin
from django.urls import path, include
from users.routers import users_router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_router.urls)),
]