from django.conf.urls import url
from maja_newsletter.views.ckeditor_utils import view_ckeditor_templates


urlpatterns = [
    url(r'^templates/$', view_ckeditor_templates, name='ckeditor_templates_list'),
]
