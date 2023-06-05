from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def create(self):
        self.save()

    def __str__(self):
        return str(self.id)