# -*- coding: utf-8 -*-
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import re
import os

def filterDateFromText(str):
    dateList = re.findall(r'\d{4}', str)
    result = ''
    if len(dateList) >= 1:
        result = dateList[0]
    return result

class Starodruk(models.Model):
    id = models.IntegerField(primary_key=True)
    autor = models.CharField(max_length=2L, blank=True)
    lp = models.CharField(max_length=3L, blank=True)
    tytul = models.CharField(max_length=767L, blank=True)
    zawartosc_strony_tytulowej = models.CharField(max_length=1371L, blank=True)
    wariant_tytulu = models.CharField(max_length=313L, blank=True)
    autor_khw = models.CharField(max_length=64L, blank=True)
    autor_dok = models.CharField(max_length=46L, blank=True)
    miejsce_wydawania = models.CharField(max_length=24L, blank=True)
    nazwa_wydawcy = models.CharField(max_length=109L, blank=True)
    data_wydania = models.CharField(max_length=30L, blank=True)
    miejsce_druku = models.CharField(max_length=22L, blank=True)
    nazwa_drukarni = models.CharField(max_length=144L, blank=True)
    data_druku = models.CharField(max_length=11L, blank=True)
    liczba_stron = models.CharField(max_length=64L, blank=True)
    oznaczenie_ilustracji = models.CharField(max_length=29L, blank=True)
    format_bibliograficzny = models.CharField(max_length=4L, blank=True)
    wpisy_wlasnosciowe = models.CharField(max_length=319L, blank=True)
    figerprint = models.CharField(max_length=33L, blank=True)
    inne = models.CharField(max_length=665L, blank=True)
    wspoltworca = models.CharField(max_length=115L, blank=True)
    slowa_kluczowe = models.CharField(max_length=165L, blank=True)
    typ_zrodla = models.CharField(max_length=18L, blank=True)
    identyfikator_zasobu = models.CharField(max_length=10L, blank=True)
    format_elektroniczny = models.CharField(max_length=10L, blank=True)
    zrodlo = models.CharField(max_length=361L, blank=True)
    kod_jezyka = models.CharField(max_length=15L, blank=True)
    nazwa_jezyka = models.CharField(max_length=31L, blank=True)
    klocek_introligatorski = models.CharField(max_length=13L, blank=True)
    sygnatura = models.CharField(max_length=12L, blank=True)
    prawa = models.CharField(max_length=10L, blank=True)
    datan_od = models.IntegerField(null=True, blank=True)
    datan_do = models.IntegerField(null=True, blank=True)
    
    @property
    def date_normalized(self):
        return filterDateFromText(self.data_druku)
        
    @property
    def title_page_path_s(self):
        key = unicode(self.lp) + '_' + self.autor
        return 'starodruki/' + key + '/' + key + '_Ss.Tyt/S.jpg'
    
    @property
    def title_page_path_m(self):
        key = unicode(self.lp) + '_' + self.autor
        return 'starodruki/' + key + '/' + key + '_Ss.Tyt/M.jpg'
    
    @property
    def get_thumbs(self):
        import stWeb
        key = unicode(self.lp) + '_' + self.autor
        thumbs = sorted(os.listdir (stWeb.__path__[0] + '/static/starodruki/' + key + '/' + key + '_T/'))
        return thumbs
    
    @property
    def get_thumbs_paths(self):
        import stWeb
        key = unicode(self.lp) + '_' + self.autor
        thumbs = sorted(os.listdir (stWeb.__path__[0] + '/static/starodruki/' + key + '/' + key + '_T/'))
        resultPaths = []
        for t in thumbs:
            resultPaths += ['starodruki/' + key + '/' + key + '_T/' + t]
        return resultPaths
        
    @property
    def get_small_paths(self):
        import stWeb
        key = unicode(self.lp) + '_' + self.autor
        thumbs = sorted(os.listdir (stWeb.__path__[0] + '/static/starodruki/' + key + '/' + key + '_S/'))
        resultPaths = []
        for t in thumbs:
            resultPaths += ['starodruki/' + key + '/' + key + '_S/' + t]
        return resultPaths
        
    @property
    def get_medium_paths(self):
        import stWeb
        key = unicode(self.lp) + '_' + self.autor
        thumbs = sorted(os.listdir (stWeb.__path__[0] + '/static/starodruki/' + key + '/' + key + '_M/'))
        resultPaths = []
        for t in thumbs:
            resultPaths += ['starodruki/' + key + '/' + key + '_M/' + t]
        return resultPaths
        
    @property
    def get_large_paths(self):
        import stWeb
        key = unicode(self.lp) + '_' + self.autor
        thumbs = sorted(os.listdir (stWeb.__path__[0] + '/static/starodruki/' + key + '/' + key + '_L/'))
        resultPaths = []
        for t in thumbs:
            resultPaths += ['starodruki/' + key + '/' + key + '_L/' + t]
        return resultPaths
    
    @property
    def get_pdf(self):
        import stWeb
        key = unicode(self.lp) + '_' + self.autor
        pdf = stWeb.__path__[0] + '/static/starodruki/starodruki_pdf/' + key + '.PDF'
        return pdf
    
    class Meta:
        db_table = 'starodruk'

