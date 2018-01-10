# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Painting

class PaintingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['painting_title']}),
        ('Painting info',   {'fields': ['painting_style', 'painting_year', 'painting_image','painting_text']}),
    ]
    list_display = ('painting_title', 'painting_style', 'painting_year', 'painting_image')


admin.site.register(Painting, PaintingAdmin)
