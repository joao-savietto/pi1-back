from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GradingViewSet

router = DefaultRouter()
router.register(r'gradings', GradingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
