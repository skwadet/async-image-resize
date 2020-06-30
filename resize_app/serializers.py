from rest_framework import serializers

from . import models


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageToResize
        fields = ['uuid', 'image', 'width', 'height']


class GetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageToResize
        fields = ['uuid', 'status', 'image']
