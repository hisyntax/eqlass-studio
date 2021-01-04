from tinymce import HTMLField
from django.db import models

# Create your models here.
class Top_photo(models.Model):
    title = models.CharField(max_length=100)
    thumbnail_1 = models.ImageField(upload_to='pics')
    thumbnail_2 = models.ImageField(upload_to='pics')
    thumbnail_3 = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title

class NoticeBoard(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()

    def __str__(self):
        return self.title


class  Video(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()

    def __str__(self):
        return self.title