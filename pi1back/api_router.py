from rest_framework.routers import DefaultRouter
from pi1back.grading.api.views import GradingViewSet, SubjectViewSet

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
router.register('gradings', GradingViewSet, basename='gradings')
router.register('subjects', SubjectViewSet, basename='subjects')

app_name = 'api'
urlpatterns = router.urls
