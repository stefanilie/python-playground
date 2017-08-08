# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader

from howmanyleft.forms import (
    SearchForm,
)

def index(request):
   if request.method == "GET":
       form = SearchForm()
       context = {
           'form': form,
       }
       return render(request, 'howmanyleft/index.html', context)