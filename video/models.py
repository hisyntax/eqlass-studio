from tinymce import HTMLField
from django.db import models

# Create your models here.
class  Upload_video(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()

    def __str__(self):
        return self.title
