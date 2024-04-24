import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
