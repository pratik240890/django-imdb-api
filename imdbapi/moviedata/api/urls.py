from django.conf.urls import url

from .views import (
        MovieListAPIView,
    )

urlpatterns = [
    url(r'^$', MovieListAPIView.as_view(), name='movies'),
]
