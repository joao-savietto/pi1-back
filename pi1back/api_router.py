from rest_framework.routers import DefaultRouter

from pi1back.users.api.views import UserViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')

app_name = 'api'
urlpatterns = router.urls