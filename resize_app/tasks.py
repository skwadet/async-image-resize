from celery import shared_task
from PIL import Image

from . import models


@shared_task
def add_resize_task(image_uuid):
    image = models.ImageToResize.objects.get(pk=image_uuid)
    resize(image)
    image.status = 'DONE'
    image.save()


def resize(image):
    image_to_resize = Image.open(str(image.image))
    resized_image = image_to_resize.resize((image.width, image.height))
    resized_image.save(str(image.image))
