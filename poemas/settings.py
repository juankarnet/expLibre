# -*- coding: utf-8 -*
from django.conf import settings

SONETO = "SON"
TERCETO = "TER"
CUARTETO = "CUA"
LIRA = "LIR"

DEFAULT_TIPOPOEMA = (
    (SONETO, "Soneto"),
    (TERCETO, "Terceto"),
    (CUARTETO, "Cuarteto"),
    (LIRA, "Lira")
)

TIPOPOEMA = getattr(settings, 'TIPOPOEMA', DEFAULT_TIPOPOEMA)

PUBLIC = "PUB"
PRIVATE = "PRI"

VISIBILITY= (
    (PUBLIC, "Pública"),
    (PRIVATE, "Privada")
)

DEFAULT_TEXT = 'Empieza a escribir, no lo pienses.'
TEXTPOEMA = getattr(settings, 'TEXTPOEMA', DEFAULT_TEXT)

BADWORDS = getattr(settings, 'PROJECT_BADWORDS', [])

