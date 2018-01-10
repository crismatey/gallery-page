# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import datetime

ACRYLIC="Acrylic"
OIL="Oil"
WATERCOLOUR="Watercolour"
PENCIL="Pencil"
OTHER="Other"

STYLE_CHOICES = (
    (ACRYLIC, "Acrylic"),
    (OIL,"Oil"),
    (WATERCOLOUR,"Watercolour"),
    (PENCIL,"Pencil"),
    (OTHER,"Other"))

class Painting(models.Model):
    painting_title = models.CharField(max_length=200)
    # file will be saved to media/documents/s
    painting_image = models.FileField(upload_to='documents')
    painting_text = models.CharField(max_length=200)
    painting_style = models.CharField(max_length=20, choices=STYLE_CHOICES, default="Other")
    painting_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(datetime.now().year)
            ],
            help_text="Use the following format: YYYY"
    )
