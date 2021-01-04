from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telphone = models.CharField(max_length=200)
    work_days_and_time = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    send_query = models.CharField(max_length=200)
    full_address =  models.CharField(max_length=200)
    website =  models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Instagram(models.Model):
    title = models.CharField(max_length=200)
    thumbnail =  models.ImageField()
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class FollowOnSocial(models.Model):
    title = models.CharField(max_length=100)
    facebookpage = models.CharField(max_length=200)
    instagramhandle = models.CharField(max_length=200)
    youtubepage = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)

    def __str__(self):
        return self.title

