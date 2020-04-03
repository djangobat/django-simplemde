from django.db import models
from django.conf import settings

from .constants import WidthChoices


class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.name


class ImageUpload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='images_created')
    image = models.ImageField(upload_to='comments/')
    width = models.IntegerField(choices=WidthChoices.CHOICES, default=WidthChoices.NAM_MUOI)
