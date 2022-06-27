from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.TextField(max_length=50,blank=True)
    body = models.TextField(max_length=300, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title