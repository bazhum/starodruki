# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns(
    '',
    (r'^$', 'stWeb.views.about'),
    (r'^about/$', 'stWeb.views.about'),
    (r'^resource/$', 'stWeb.views.resource'),
    (r'^search/$', 'stWeb.views.searchAdv'),
    (r'^search/results/$', 'stWeb.views.searchResults'),
    (r'^listNames/([a-zA-Z\#]){1}/(\d+)/$', 'stWeb.views.listNames'),
    (r'^browse/$', 'stWeb.views.browse'),
    (r'^single/(\d+)/$', 'stWeb.views.single'),
    (r'^thumbnails/(\d+)/(\d+)/$', 'stWeb.views.showThumbnails'),
    (r'^zoom/(\d+)/(\d+)/$', 'stWeb.views.zoom'),
    (r'^double/(\d+)/(\d+)/$', 'stWeb.views.double'),
    (r'^download/$', 'stWeb.views.download'),
)