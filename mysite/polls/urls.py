from django.conf.urls import url

# importing the views file
from . import views

# maping the /index url
urlpatterns = [
    url(r'^$', views.index, name='index')
]