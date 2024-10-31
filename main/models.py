from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    uploadted_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title