# youtube-django

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