from django.db import models

# Create your models here.
class UserDetails(models.Model):
    """ Basic User details"""
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    android_token = models.CharField(max_length=100, default=0)
    ios_token = models.CharField(max_length=100, default=0)
    desktop_token = models.CharField(max_length=100, default=0)
    email_verified = models.CharField(max_length=10, default='no')
    signin_on = models.CharField(max_length=50)
    class Meta:
        db_table = "user_details"

class LinkDetails(models.Model):
    """ Link Details """
    url = models.TextField()
    user_id = models.IntegerField()
    title = models.TextField(default='This is Title')
    description = models.TextField(default='This is Description')
    image = models.TextField(
        default=
        '''http://tamil.thehindu.com/multimedia/dynamic/02444/high_court_madurai_2444480f.jpg'''
        )
    body = models.TextField(default='')
    submitted_on = models.CharField(max_length=50)
    class Meta:
        db_table = "link_details"
