from django.db import models
from django.contrib.auth.models import User

# date and time is not accurate

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Attachment(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
