from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Posts(models.Model):
    image = models.ImageField(null=True, upload_to='images/', height_field=None, width_field=None, max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

