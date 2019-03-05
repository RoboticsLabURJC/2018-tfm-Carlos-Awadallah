# -*- coding: utf-8 -*-

from django.conf.urls import *

from . import views

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

	url(r'^$', views.index), # Página Principal de la Aplicación
	url(r'^main_page', views.main_page, name='exercises'), # Main page. List of practices
    url(r'^local', views.local, name='local'), # Local Execution Page

]

