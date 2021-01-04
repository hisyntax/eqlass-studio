from django.db import models

# Create your models here.
class Wedding(models.Model):
    thumbnail = models.ImageField(upload_to='pics')
    overview = models.TextField()

    def __str__(self):
        return self.overview


class Other(models.Model):
    thumbnail = models.ImageField(upload_to='pics')
    overview = models.TextField()

    def __str__(self):
        return self.overview


class List_of_service(models.Model):
    list = models.CharField(max_length=100)


    def __str__(self):
        return self.list