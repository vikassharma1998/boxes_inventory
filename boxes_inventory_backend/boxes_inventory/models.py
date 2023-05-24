from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Box(models.Model):
    length = models.FloatField()
    breadth = models.FloatField()
    height = models.FloatField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_boxes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Box ({self.id})"


class BoxUpdate(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='updates')
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='box_updates')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Box Update ({self.id})"