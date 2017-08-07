from django.conf.urls import url 

from . import views
from howmanyleft.views import (
    index,
)

urlpatterns = [
    url(r'^$', index, name='index'),
]