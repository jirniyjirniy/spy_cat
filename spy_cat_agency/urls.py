from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agency.views import SpyCatViewSet, MissionViewSet

router = DefaultRouter()
router.register(r'spycats', SpyCatViewSet)
router.register(r'missions', MissionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
