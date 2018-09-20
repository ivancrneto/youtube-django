from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import VideoUploadView

urlpatterns = [
    path('upload', VideoUploadView.as_view(), name='video_upload')
]
