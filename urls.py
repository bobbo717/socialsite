from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'socialsite.views.home', name='home'),
    # url(r'^social_site/', include('social_site.foo.urls')),

    url(r'^facebook/login$', 'socialsite.facebook.views.login'),
    url(r'^facebook/authentication_callback$', 'socialsite.facebook.views.authentication_callback'),
    url(r'^facebook/friends$', 'socialsite.views.fb_friends'),

    url(r'^account/(?P<user_id>\d+)/following/$', 'socialsite.views.follow_list'),
    url(r'^account/(?P<user_id>\d+)/follow/(?P<following_id>\d+)/$', 'socialsite.views.user_follow'),
    url(r'^account/(?P<user_id>\d+)$', 'socialsite.views.user'),
    url(r'^account/accounts$', 'socialsite.views.available_users'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
