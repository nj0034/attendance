from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class AttendanceUser(models.Model):
    TYPE = (
        ('professor', '교수'),
        ('student', '학생')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices=TYPE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         AttendanceUser.objects.create(user=instance, type='', name=instance.username)

