from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Write(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    images = models.ImageField(null=True, blank=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Write, related_name="comment", on_delete=CASCADE)
    user = models.ForeignKey(User,related_name="comment", on_delete=CASCADE)
    content = models.TextField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

class Map(models.Model):
    objects = models.Manager()
    input_memo = models.CharField(max_length=200, null=True)
    lat=models.DecimalField(max_digits=9,decimal_places=6, null=True)
    lon=models.DecimalField(max_digits=9,decimal_places=6, null=True)
    placename=models.CharField(max_length=100 , null=True)
    post=models.ForeignKey(Write,related_name="report",on_delete=CASCADE,null=True)