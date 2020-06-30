from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView

from . import models
from . import serializers


class CreateTaskAPI(viewsets.ModelViewSet):
    queryset = models.ImageToResize.objects.all()
    serializer_class = serializers.CreateTaskSerializer
    http_method_names = ['post']


class GetStatusAPI(RetrieveAPIView):
    queryset = models.ImageToResize.objects.all()
    serializer_class = serializers.GetStatusSerializer
    http_method_names = ['get']
