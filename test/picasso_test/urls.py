from django.contrib import admin
from django.urls import path

from files.views import FilesView, UploadView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('files/', FilesView.as_view(), name='upload'),
    path('upload/', UploadView.as_view(), name='upload'),
]
