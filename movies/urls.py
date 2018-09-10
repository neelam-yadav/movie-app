from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    MovieCreate,
    MovieSearchList
)

app_name = 'Movie'
urlpatterns = [
    url(
        regex='^$',
        view=MovieSearchList.as_view(),
        name='list'),
    url(
        regex='^create/',
        view=MovieCreate.as_view(),
        name='create'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
