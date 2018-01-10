# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Painting
import datetime

def index(request):
    painting_list = Painting.objects.order_by('-id')
    context = {'painting_list': painting_list}
    return render(request, 'gallery/index.html', context)


def detail(request, painting_id):
    try:
        painting = Painting.objects.get(pk=painting_id)
    except Painting.DoesNotExist:
        raise Http404('Painting does not exist')
    return render(request, 'gallery/detail.html', {'painting':painting})
