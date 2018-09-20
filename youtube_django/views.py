from django.shortcuts import render
from django.views.generic import TemplateView


class VideoUploadView(TemplateView):
    template_name = 'youtube_django/upload.html'
