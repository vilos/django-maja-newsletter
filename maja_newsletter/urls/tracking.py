"""Urls for the maja_newsletter Tracking"""
from django.conf.urls import url
from maja_newsletter.views import tracking


urlpatterns = [
    url(r'^newsletter/(?P<slug>[-\w]+)/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)\.(?P<format>png|gif|jpg)$',
        tracking.view_newsletter_tracking,
        name='newsletter_newsletter_tracking'),
    url(r'^link/(?P<slug>[-\w]+)/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/(?P<link_id>\d+)/$',
        tracking.view_newsletter_tracking_link,
        name='newsletter_newsletter_tracking_link'),
    url(r'^historic/(?P<slug>[-\w]+)/$',
        tracking.view_newsletter_historic,
        name='newsletter_newsletter_historic')
]
