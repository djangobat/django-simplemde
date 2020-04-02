from django.db import models
from django.conf import settings


class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ImageUpload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='images_created')
    image = models.ImageField(upload_to='comments/')
