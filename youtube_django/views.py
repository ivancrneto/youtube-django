import tempfile
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets, OAuth2WebServerFlow
from oauth2client.contrib import xsrfutil
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from .models import GoogleAPIOauthInfo


class YouTubeForm(forms.Form):
    video = forms.FileField()


class VideoUploadView(FormView):
    template_name = 'youtube_django/upload.html'
    form_class = YouTubeForm

    def form_valid(self, form):
        fname = form.cleaned_data['video'].temporary_file_path()

        storage = DjangoORMStorage(
            GoogleAPIOauthInfo, 'id', self.request.user.id, 'credentials')
        credentials = storage.get()

        client = build('youtube', 'v3', credentials=credentials)

        body = {
            'snippet': {
                'title': 'My Django Youtube Video',
                'description': 'My Django Youtube Video Description',
                'tags': 'django,howto,video,api',
                'categoryId': '27'
            },
            'status': {
                'privacyStatus': 'unlisted'
            }
        }

        with tempfile.NamedTemporaryFile('wb', suffix='yt-django') as tmpfile:
            with open(fname, 'rb') as fileobj:
                tmpfile.write(fileobj.read())
                insert_request = client.videos().insert(
                    part=','.join(body.keys()),
                    body=body,
                    media_body=MediaFileUpload(
                        tmpfile.name, chunksize=-1, resumable=True)
                )
                insert_request.execute()

        return HttpResponse('It worked!')


# flow variable stays as global for now
flow = None


class AuthorizeView(View):

    def get(self, request, *args, **kwargs):
        storage = DjangoORMStorage(
            GoogleAPIOauthInfo, 'id', request.user.id, 'credentials')
        credentials = storage.get()

        global flow
        flow = OAuth2WebServerFlow(
            client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
            client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            scope='https://www.googleapis.com/auth/youtube',
            redirect_uri=request.build_absolute_uri(
                reverse(settings.GOOGLE_OAUTH2_CALLBACK_VIEW)))
        # TODO: for a downloaded the client_secrets file
        '''flow = flow_from_clientsecrets(
            settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
            scope='https://www.googleapis.com/auth/youtube',
            redirect_uri=request.build_absolute_uri(
                reverse(settings.GOOGLE_OAUTH2_CALLBACK_VIEW)))'''

        if credentials is None or credentials.invalid:
            flow.params['state'] = xsrfutil.generate_token(
                settings.SECRET_KEY, request.user)
            authorize_url = flow.step1_get_authorize_url()
            return redirect(authorize_url)
        return redirect('/upload/')


class Oauth2CallbackView(View):

    def get(self, request, *args, **kwargs):
        if not xsrfutil.validate_token(
            settings.SECRET_KEY, request.GET.get('state').encode(),
            request.user):
                return HttpResponseBadRequest()
        global flow
        credentials = flow.step2_exchange(request.GET)
        storage = DjangoORMStorage(
            GoogleAPIOauthInfo, 'id', request.user.id, 'credentials')
        storage.put(credentials)
        return redirect('/upload/')
