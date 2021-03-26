import os

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Shoe


# Delete image signal
@receiver(post_delete, sender=Shoe)
def auto_post_delete_shoe_image(instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


# @receiver(post_save, sender=Shoe)
# def auto_post_delete_old_shoe_image(instance, **kwargs):
#     if instance.image:
#         if os.path.isfile(instance.image.path):
#             os.remove(instance.image.path)

# @receiver(post_save, sender=Shoe)
# def alert_post_save_new_shoe(created, instance, **kwargs):
#     if created:
#         print(f'Object {instance.model} has been created')




