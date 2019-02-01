# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from poemas.settings import TIPOPOEMA,VISIBILITY, PUBLIC, TEXTPOEMA
from poemas.validators import badwords_detector


class Poema(models.Model):

    owner = models.ForeignKey(User)
    nombre = models.CharField(max_length=150)
    titulo = models.CharField(max_length=300)
    texto = models.TextField(default=TEXTPOEMA, validators=[badwords_detector])
    url = models.URLField(blank=True)
    tags = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=3, choices=TIPOPOEMA)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __unicode__(self): #Method de 0 params
        return self.nombre
