from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from .serializers import CreateUserSerializer, GenericUserSerializer
from ...shared.permissions import IsAuthenticated

User = get_user_model()

class UserViewSet(ModelViewSet):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return CreateUserSerializer(*args, **kwargs)
        return GenericUserSerializer(*args, **kwargs)

