# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from poemas.models import Poema

class PoemaAdmin(admin.ModelAdmin):
    list_display = ('nombre','titulo', 'owner_name', 'tipo', 'visibility')
    list_filter = ('visibility', 'tipo')
    search_fields = ('nombre', 'titulo')

    def owner_name(self, obj):
        return obj.owner.first_name + u' ' + obj.owner.last_name
    owner_name.short_description = u'Poema owner'
    owner_name.admin_order_field = 'owner'

    fieldsets = (
        (None, {
            'fields': ('nombre',),
            'classes': ('wide',)
        }),
        ('Description & Author', {
            'fields': ('titulo', 'texto', 'tags'),
            'classes': ('wide')
        }),
        ('Extra', {
            'fields': ('url', 'tipo', 'visibility'),
            'classes': ('wide', 'collapse')
        })
    )

admin.site.register(Poema, PoemaAdmin)
