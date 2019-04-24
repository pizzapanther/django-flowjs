from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from views import UploadView, CheckStateView

# JSON REQUESTS
urlpatterns = patterns('',
    url(r'^upload/$', csrf_exempt(UploadView.as_view())),
    url(r'^state/$', csrf_exempt(CheckStateView.as_view())),
)
