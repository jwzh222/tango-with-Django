#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))
