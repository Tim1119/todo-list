from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("home")

    
    