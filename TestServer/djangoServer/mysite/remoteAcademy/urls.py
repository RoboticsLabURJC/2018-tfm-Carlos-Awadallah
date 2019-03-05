# -*- coding: utf-8 -*-

from django.conf.urls import *

from . import views

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

	url(r'^$', views.index), # Página Principal de la Aplicación
	#url(r'^login', views.login), # Login en la Aplicación
	#url(r'^logout', views.logout), # Logout de la Aplicación
	#url(r'^registration', views.registration), # Logout de la Aplicación
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  views.activate, name="activate"),
	#url(r'^config', views.config), # Menú de configuración de la aplicación
	#url(r'^users', views.users), # Vista con el listado de todos los usuarios de la App
	#url(r'^update_exercises', views.update_exercises), # Actualiza la lista de ejercicios
	#url(r'^kill_user_simulations', views.kill_user_simulations),
	#url(r'^kill_simulation/(?P<container_id>[0-9A-Za-z_\-]+)', views.stop_simulation),
	#url(r'^reboot_app', views.reboot_app), # Actualiza la lista de ejercicios
	#url(r'^testing', views.testing), # Actualiza la lista de ejercicios
	url(r'^main_page', views.main_page, name='exercises'), # Main page. List of practices
    url(r'^local', views.local, name='local'), # Main page. List of practices
    url(r'^logout', views.logout, name='logout'),
	#url(r'^simulation/(?P<exercise_id>[\w\-]+)/(?P<simulation_type>[\w\-]+)', views.simulation_exercise), # Simulation

	# ===== Recuperación de Contraseñas ======
	#url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'reset_password/password_reset_form.html'}, name='password_reset'),
    #url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'reset_password/password_reset_done.html'}, name='password_reset_done'),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #auth_views.password_reset_confirm, {'template_name': 'reset_password/password_reset_confirm.html'}, name='password_reset_confirm'),
    #url(r'^reset/done/$', auth_views.password_reset_complete,{'template_name': 'reset_password/password_reset_complete.html'}, name='password_reset_complete'),

]

