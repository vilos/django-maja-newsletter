"""Urls for the maja_newsletter Newsletter"""
from django.conf.urls import url
from maja_newsletter.views import newsletter


urlpatterns = [
    url(r'^preview/(?P<slug>[-\w]+)/$',
        newsletter.view_newsletter_preview,
        name='newsletter_newsletter_preview'),
    url(r'^(?P<slug>[-\w]+)/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        newsletter.view_newsletter_contact,
        name='newsletter_newsletter_contact'),
]
