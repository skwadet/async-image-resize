from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save

from . import models
from . import tasks


@receiver(post_save, sender=models.ImageToResize)
def resize_signal(sender, instance, **kwargs):
    if instance.status == 'NOT DONE':
        transaction.on_commit(lambda: tasks.add_resize_task.delay(image_uuid=instance.uuid))
