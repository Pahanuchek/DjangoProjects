from django.db import models

class Humans(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(blank=None)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
