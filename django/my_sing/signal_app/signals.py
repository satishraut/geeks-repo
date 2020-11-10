from django.db.models.signals import post_save, pre_save, pre_delete
from .models import Post, Profile
from django.contrib.auth.models import User 
from django.dispatch import receiver, Signal


def save_post(sender,instance,**kwargs):
    print('Saved Post Succsuufully')

def save_pre(sender,instance,**kwargs):
    print("Pre save in progress")

def delete_pre(sender,instance,**kwargs):
    print("Post deleted")

post_save.connect(save_post, sender=Post)
pre_save.connect(save_pre, sender=Post)
pre_delete.connect(delete_pre, sender=Post)


@receiver(post_save, sender=User)
def prof(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)