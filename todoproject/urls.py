from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from todos.views import TodoViewSet, health, home

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"todos", TodoViewSet)

urlpatterns = [
    path("", home),
    path("health", health),
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
