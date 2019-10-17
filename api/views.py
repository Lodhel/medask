from rest_framework import viewsets

from . import models, serializers


class MainViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MainSerializer
    queryset = models.Main.objects.all()