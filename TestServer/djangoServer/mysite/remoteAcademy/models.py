# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    host = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    max_simulations = models.IntegerField(default=0)
    running_simulations = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.host

class Simulation(models.Model):
    user = models.CharField(max_length=200)
    init_simulation = models.CharField(max_length=200)
    simulation_type = models.CharField(max_length=200)
    exercise = models.CharField(max_length=200)
    docker_id = models.CharField(max_length=200)
    client_ip = models.CharField(max_length=200)
    main_server_ip = models.CharField(max_length=200)
    host_ip = models.CharField(max_length=200)
    ws_channel = models.CharField(max_length=200)

