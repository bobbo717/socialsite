import json, urllib, datetime

from django.db import models
from django.contrib.auth.models import User

class FacebookProfile(models.Model):
    user = models.OneToOneField(User)
    facebook_id = models.BigIntegerField()
    access_token = models.CharField(max_length=150)


    def get_facebook_profile(self):
        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % self.access_token)
        return json.load(fb_profile)

    def get_facebook_friends(self):
        fb_friends = urllib.urlopen('https://graph.facebook.com/me/friends/?access_token=%s' % self.access_token)
        return json.load(fb_friends)

class FacebookFriends(models.Model):
    user = models.ForeignKey(User)
    facebook_id = models.BigIntegerField()
    name = models.CharField(max_length=75)
    class Meta:
        unique_together = (("user", "facebook_id"),)

class UserFollows(models.Model):
    user = models.ForeignKey(User, related_name="_unused_")
    following = models.ForeignKey(User, related_name="following")
    added = models.DateField(default=datetime.date.today)
    class Meta:
        unique_together = (("user", "following"),)
