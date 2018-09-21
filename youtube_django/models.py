from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField


class GoogleAPIOauthInfo(models.Model):
    credentials = CredentialsField()
