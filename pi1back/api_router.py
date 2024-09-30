from rest_framework.routers import DefaultRouter

from pi1back.users.api.views import UserViewSet
from pi1back.occurrences.api.views import (    
    OccurrenceViewSet
)
from pi1back.classrooms.api.views import (
    ClassroomViewSet
)

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('occurrences', OccurrenceViewSet, basename='occurrences')
router.register('classrooms', ClassroomViewSet, basename='classrooms')

app_name = 'api'
urlpatterns = router.urls