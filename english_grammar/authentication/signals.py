from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_default_grouo(sender, instance, created, **kwargs):
      if created:
        default_group, _ = Group.objects.get_or_create(name='Student')
        instance.groups.add(default_group)


