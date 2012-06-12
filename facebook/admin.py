from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import FacebookProfile, FacebookFriends, UserFollows

# We want to display our facebook profile, not the default user
admin.site.unregister(User)

class FacebookProfileInline(admin.StackedInline):
    model = FacebookProfile

class FacebookFriendsInline(admin.StackedInline):
    model = FacebookFriends

class FacebookProfileAdmin(UserAdmin):
    inlines = [FacebookProfileInline,FacebookFriendsInline]

admin.site.register(User, FacebookProfileAdmin)

