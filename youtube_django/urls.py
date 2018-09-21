from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AuthorizeView, Oauth2CallbackView,  VideoUploadView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video_upload'),
    path('authorize/', AuthorizeView.as_view(), name='authorize'),
    path('oauth2callback/', Oauth2CallbackView.as_view(),
         name='oauth2callback')
]
