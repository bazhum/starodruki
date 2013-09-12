# -*- coding: utf-8 -*-

from metadane.models import Starodruk
import re
from django.db.models import Q

def truncate_string(mystring, numberofwords): 
    return ' '.join(mystring.split()[:numberofwords])

def filterDateFromText(str):
    dateList = re.findall(r'\d{4}', str)
    result = ''
    if len(dateList) >= 1:
        result = dateList[0]
    return result

def processQuery(request):
    type = request.GET.get('type', '')
#     query = request.GET.get('query', '')
    qs = Starodruk.objects.all()
    if type == 'simple':
        query = request.GET.get('query', '')
        qObjs = Q(tytul__search=query) | Q(zawartosc_strony_tytulowej__search=query) | Q(autor_dok__search=query) | Q(autor_khw__search=query) 
        qs = qs.filter(qObjs)
    elif type == 'all':
        orderby = request.GET.get('order', 'autor_dok')
        if orderby == 'data_wydania' or orderby == '-data_wydania':
#             sql_normalize = "(CASE WHEN data_wydania REGEXP '[-]' THEN replace(replace(replace(replace(substr(data_wydania, 0, locate('-', data_wydania)), '[', ''), ']', ''), 'post', ''), ' ', '') ELSE replace(replace(replace(replace(data_wydania, '[', ''), ']', ''), 'post', ''), ' ', '') END)"            
#             qs = qs.extra(select={'data_normalized': sql_normalize}).extra(order_by=[orderby.replace('data_wydania', 'data_normalized')])
            qs = qs.extra(order_by=[orderby.replace('data_wydania', 'datan_od')])
        else:
            qs = qs.order_by(orderby)   
    elif type == 'adv':
        if 'autor' in request.GET:
            if request.GET['autor'] != '':
                qs = qs.filter(Q(autor_dok__search=request.GET['autor']) | Q(autor_khw__search=request.GET['autor']))
        if 'tytul' in request.GET:
            if request.GET['tytul'] != '':
                qs = qs.filter(tytul__search=request.GET['tytul'])
        if 'miejsce' in request.GET:
            if request.GET['miejsce'] != '':
                qs = qs.filter(miejsce_wydawania__icontains=request.GET['miejsce'])
        if 'dataOd' in request.GET:
            if request.GET['dataOd'] != '':
#                 sql_normalize = "(CASE WHEN data_wydania REGEXP '[-]' THEN replace(replace(replace(replace(substr(data_wydania, 0, locate('-', data_wydania)), '[', ''), ']', ''), 'post', ''), ' ', '') ELSE replace(replace(replace(replace(data_wydania, '[', ''), ']', ''), 'post', ''), ' ', '') END)"
#                 qs = qs.extra(where=[sql_normalize + " >= " + request.GET['dataOd']])
                sql_normalize = '(datan_od >= ' + request.GET['dataOd'] + ' OR datan_do >= ' + request.GET['dataOd'] + ")" 
                qs = qs.extra(where=[sql_normalize])
                # qs = qs.filter(date_normalized__gte=filterDateFromText(request.GET['dataOd']))
        if 'dataDo' in request.GET:
            if request.GET['dataDo'] != '':
#                 sql_normalize = "(CASE WHEN data_wydania REGEXP '[-]' THEN replace(replace(replace(replace(substr(data_wydania, 0, locate('-', data_wydania)), '[', ''), ']', ''), 'post', ''), ' ', '') ELSE replace(replace(replace(replace(data_wydania, '[', ''), ']', ''), 'post', ''), ' ', '') END)"
#                 qs = qs.extra(where=[sql_normalize + " <= " + request.GET['dataDo']])
                sql_normalize = '(datan_od <= ' + request.GET['dataDo'] + ' OR datan_do <= ' + request.GET['dataDo'] + ")" 
                qs = qs.extra(where=[sql_normalize])
                # qs = qs.filter(date_normalized__lte=filterDataFromText(request.GET['dataDo']))
        if 'wydawca' in request.GET:
            if request.GET['wydawca'] != '':
                qs = qs.filter(nazwa_wydawcy__icontains=request.GET['wydawca'])
        if 'sygnatura' in request.GET:
            if request.GET['sygnatura'] != '':
                qs = qs.filter(sygnatura__icontains=request.GET['sygnatura'])
            
    return qs

def searchDescription(request):
    type = request.GET.get('type', '')
    opis = 'Wyniki wyszukiwania dla '
    if type == 'simple':
        opis += request.GET.get('query', '')
    elif type == 'adv':
        opis += ": "
        objList = []
        for k,v in request.GET.iteritems():
            objList += [(k,v)]
        objList.reverse()
        for k,v in objList:
            if k not in ['pageNo', 'type', 'view']:
                if v != '':
                    if opis[opis.__len__()-1:opis.__len__()] == ',':
                        opis += " "
                    if k == 'dataDo':
                        opis +=  u'data do: “' + v + u'”,'
                    elif k == 'dataOd':
                        opis +=  u'data od: “' + v + u'”,'
                    else:
                        opis += k + u': “' + v + u'”,'
        opis = opis[0:opis.__len__()-1]
    
    return opis