from rest_framework.viewsets import GenericViewSet
from .models import Men
from .serializer import MenSerializer
from rest_framework import mixins


class MenViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    queryset = Men.objects.all()
    serializer_class = MenSerializer