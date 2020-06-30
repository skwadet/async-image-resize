import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ImageToResize(models.Model):
    STATUS_CHOICE = [
        ('DONE', 'Done'),
        ('NOT DONE', 'Not done')
    ]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')
    width = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)])
    height = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)])
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=25, default='NOT DONE', blank=True)

    def __str__(self):
        return 'Image {uuid}'.format(uuid=self.uuid)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
