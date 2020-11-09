from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.PlaylistViewSet)
urlpatterns = [
    path('', include(router.urls))
]
