# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from poemas.models import Poema
from poemas.settings import BADWORDS


class PoemaForm(forms.ModelForm):
    """
    Formulario para el modelo Poema
    """
    class Meta:
        model = Poema
        exclude = ['owner']
        

    # def clean(self):
    #     """
    #     Valida si en la restricción se han puesto palabras para controlar
    #     :return:
    #     """
    #     cleaned_data = super(PoemaForm, self).clean()
    #     text_poema = cleaned_data.get('texto', '')
    #
    #     for badword in BADWORDS:
    #         if badword.lower() in text_poema.lower():
    #             raise(ValidationError(u'La palabra "{0}", no está permitida'.format(badword)))
    #
    #     return cleaned_data