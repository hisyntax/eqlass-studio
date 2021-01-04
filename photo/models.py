from django.db import models

# Create your models here.
class Photo(models.Model):
    thumbnail = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=200)


    def __str__(self):
        return self.title