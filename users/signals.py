from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Check if the user has a profile; if not, create one
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        # If the user doesn't have a profile, create it
        Profile.objects.create(user=instance)

    