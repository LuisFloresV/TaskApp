from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

class Task(models.Model):
    User = settings.AUTH_USER_MODEL
    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
    
    
