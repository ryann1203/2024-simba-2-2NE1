from django.db import models

# Create your models here.
class Varsity(models.Model):
    major=models.CharField(max_length=20)
    like_count=models.PositiveIntegerField(default=0)
    image_front=models.ImageField(null=True)
    image_back=models.ImageField(null=True)