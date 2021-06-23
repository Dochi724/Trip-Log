from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=CASCADE, related_name='pro')
    nickname = models.CharField(max_length=10)
    GENDER_CHOICES = (
        ('여', '여'),
        ('남', '남')
    )
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=14)
    like_post = models.ManyToManyField(
        'main.Write', related_name='like_users', null=True, blank=True)

    def __str__(self):
        return str(self.user)
