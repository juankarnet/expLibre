# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError

from poemas.settings import BADWORDS


def badwords_detector(value):
    """
    Valida si en la value se han puesto tacos definidos en BADWORDS
    :return:Boolean
    """

    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise (ValidationError(u'La palabra "{0}", no está permitida'.format(badword)))

    #Si todo va bien devuelvo true
    return True