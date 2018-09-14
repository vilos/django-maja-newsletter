"""Urls for the maja_newsletter statistics"""
from django.conf.urls import url
from maja_newsletter.views import statistics


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$',
        statistics.view_newsletter_statistics,
        name='newsletter_newsletter_statistics'),
    url(r'^report/(?P<slug>[-\w]+)/$',
        statistics.view_newsletter_report,
        name='newsletter_newsletter_report'),
    url(r'^charts/(?P<slug>[-\w]+)/$',
        statistics.view_newsletter_charts,
        name='newsletter_newsletter_charts'),
    url(r'^density/(?P<slug>[-\w]+)/$',
        statistics.view_newsletter_density,
        name='newsletter_newsletter_density'),
]
