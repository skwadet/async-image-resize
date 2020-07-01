from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework_tracking.mixins import LoggingMixin

from . import models
from . import serializers


class CreateTaskAPI(LoggingMixin, viewsets.ModelViewSet):
    logging_methods = ['POST', 'PUT', 'PATCH', 'UPDATE', 'GET', 'DELETE']
    queryset = models.ImageToResize.objects.all()
    serializer_class = serializers.CreateTaskSerializer
    http_method_names = ['post']


class GetTaskAPI(RetrieveAPIView):
    logging_methods = ['POST', 'PUT', 'PATCH', 'UPDATE', 'GET', 'DELETE']
    queryset = models.ImageToResize.objects.all()
    serializer_class = serializers.GetTaskSerializer
    http_method_names = ['get']
