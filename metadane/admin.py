# -*- coding: utf-8 -*-

from django.contrib import admin
from metadane.models import *

class stAdmin(admin.ModelAdmin):
	list_display = ['tytul', 'data_druku', 'liczba_stron', 'typ_zrodla', 'kod_jezyka']
	list_filter = ['typ_zrodla', 'kod_jezyka']
	search_fields = ['tytul', 'data_druku', 'liczba_stron', 'typ_zrodla', 'kod_jezyka']

admin.site.register(Starodruk, stAdmin)
