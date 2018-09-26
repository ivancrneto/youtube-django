# youtube-django


|       |  |
| ----------- | ----------- |
| docs      | ![Documentation Status](https://readthedocs.org/projects/youtube-django/badge/?style=flat)      |
| tests   |[![CircleCI](https://circleci.com/gh/ivancrneto/youtube-django.svg?style=svg)](https://circleci.com/gh/ivancrneto/youtube-django) [![codecov](https://codecov.io/gh/ivancrneto/youtube-django/branch/master/graph/badge.svg)](https://codecov.io/gh/ivancrneto/pymox) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/399d643486d74d7eafd27e7dbac698c8)](https://www.codacy.com/app/ineto/youtube-django?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ivancrneto/youtube-django&amp;utm_campaign=Badge_Grade) ![Requirements Status](https://requires.io/github/ivancrneto/youtube-django/requirements.svg?branch=master)       |
| package   |   ![PyPI Package latest release](https://img.shields.io/pypi/v/youtube-django.svg) ![PyPI Wheel](https://img.shields.io/pypi/wheel/youtube-django.svg) ![Supported versions](https://img.shields.io/pypi/pyversions/pytest-cov.svg) ![Supported implementations](https://img.shields.io/pypi/implementation/youtube-django.svg) ![Commits since latest release](https://img.shields.io/github/commits-since/ivancrneto/youtube-django/0.1.svg)       |


## Install

``` bash
$ pip install youtube-django
```

Add `'youtube_django'` to your settings.

``` python
INSTALLED_APPS = [
    # [...]
    'youtube_django',
]
```

Run migrations:

``` bash
$ python manage.py migrate
```

Add the following Google Oauth Settings to your `settings.py`:

```
GOOGLE_OAUTH2_CLIENT_ID = '<Your Client ID from Google Developer Console>'
GOOGLE_OAUTH2_CLIENT_SECRET = '<Your Client Secret from Google Developer Console>'
GOOGLE_OAUTH2_CALLBACK_VIEW = 'oauth2callback'  # your oauth callback view name
```

Add your views.Example:

```python
from youtube_django.views import (
    VideoUploadView,
    AuthorizeView,
    Oauth2CallbackView,
)

urlpatterns = [
    path('^yt/upload/', VideoUploadView.as_view(), name='video_upload'),
    path('^yt/authorize/', AuthorizeView.as_view(), name='authorize'),
    path('^yt/oauth2callback/', Oauth2CallbackView.as_view(),
        name='oauth2callback')
]
```