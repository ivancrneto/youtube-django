from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AuthorizeView, VideoUploadView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video_upload'),
    path('authorize/', AuthorizeView.as_view(), name='authorize'),
]
