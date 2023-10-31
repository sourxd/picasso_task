from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from files.views import files_view, upload_view, FilesView, UploadView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('files/', FilesView.as_view(), name='upload'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('visual/files_view/', files_view, name='files_view'),
    path('visual/upload_view/', upload_view, name='upload_view'),
]
