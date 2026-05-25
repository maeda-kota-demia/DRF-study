from django.db import models

# api/models.py
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass

class Todo(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos'
    )
    title = models.CharField(max_length=100)
    is_done = models.BooleanField()

    def __str__(self):
        return self.title