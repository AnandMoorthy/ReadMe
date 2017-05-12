from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    token = models.CharField(max_length=100,default=0)
    signin_on = models.CharField(max_length=50)
    class Meta:
        db_table = "user_details"

class LinkDetails(models.Model):
    url = models.TextField()
    title = models.TextField(default=None)
    description = models.TextField(default=None)
    body = models.TextField(default=None)
    image_link = models.TextField(default=None)
    user_id = models.IntegerField()
    submitted_on = models.CharField(max_length=50)
    class Meta:
        db_table = "link_details"
