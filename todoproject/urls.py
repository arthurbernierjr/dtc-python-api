from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from todos.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r"todos", TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
