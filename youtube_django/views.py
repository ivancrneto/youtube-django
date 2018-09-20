from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView



class YouTubeForm(forms.Form):
    pass


class VideoUploadView(FormView):
    template_name = 'youtube_django/upload.html'
    form_class = YouTubeForm
