from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

