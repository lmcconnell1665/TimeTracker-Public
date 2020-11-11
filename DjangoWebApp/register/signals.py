from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This runs every time a user is created to make that user a profile
@receiver(post_save, sender=User) #when a user is saved then send this signal
def create_profile(sender, instance, created, **kwargs): #which is received by this sender
    if created: #if the user we saved was just created
        Profile.objects.create(user=instance) #create them a profile

# This runs every time a user profile is saved
@receiver(post_save, sender=User) #when a user is saved then send this signal
def save_profile(sender, instance, **kwargs): #which is received by this sender
    instance.profile.save() #save the profile