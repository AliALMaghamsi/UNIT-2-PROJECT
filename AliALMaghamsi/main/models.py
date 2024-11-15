from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=512)
    last_name=models.TextField(max_length=512)
    email=models.EmailField(max_length=512)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=timezone.now)