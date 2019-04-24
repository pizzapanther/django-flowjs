from django.urls import path, re_path, include
from django.views.decorators.csrf import csrf_exempt

from views import UploadView, CheckStateView

app_name = 'flowjs'

# JSON REQUESTS
urlpatterns = [
    re_path(r'^upload/$', csrf_exempt(UploadView.as_view())),
    re_path(r'^state/$', csrf_exempt(CheckStateView.as_view())),
]
