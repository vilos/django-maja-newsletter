from django.conf.urls import url
from maja_newsletter.views import tinymce_utils

urlpatterns = [
    url(r'^templates/$', tinymce_utils.view_tinymce_templates, name='tinymce_templates_list'),
]
