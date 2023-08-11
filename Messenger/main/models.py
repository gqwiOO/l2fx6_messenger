from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# it's a model for messages

class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')





