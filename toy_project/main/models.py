from django.db import models
# Create your models here.


class Write(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    images = models.ImageField(null=True, blank=True, upload_to="user_images")
    updated_at = models.DateTimeField(auto_now=True)
