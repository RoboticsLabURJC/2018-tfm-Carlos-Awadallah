# -*- coding: utf-8 -*-

from django.shortcuts import render
import json
import io
import os

tk = 0
kernel_port = 0
session = 0

class Exercise():
    def __init__(self, name, img):
        self.name = name
        self.img = img
    def get_src(self):
        return "/static/remoteAcademy/images/portfolio/"+self.img

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    """ Página comercial de la Aplicación """

    context = {
        "authenticate": False
    }
    return render(request, 'remoteAcademy/index.html', context)

def main_page(request):
    """ Página principal de la Aplicación - Ejercicios"""

    if request.method == 'GET':
        ### Página de ejercicios ###
        # lista de ejericios
        cf = Exercise('Color Filter', 'portfolio_color_filter.png')
        exercises_list = [cf]
        context = {
            "message": "Hi! Welcome to JdeRobot Academy Web!",
            "exercises_list": exercises_list,
        }
    elif request.method == 'POST':
        ### Al salir de un ejercicio ###
        # Obtener Notebook e identificador de sesión
        filled_notebook = request.POST['filledNotebook'] 
        kernel_session = request.POST['kernelSession']   
        # Guardar el Notebook Relleno en el servidor web
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, 'color_filter.ipynb'), 'w') as nb:
            nb.write(filled_notebook)
        nb.close()

        # lista de ejercicios
        cf = Exercise('Color Filter', 'portfolio_color_filter.png')
        exercises_list = [cf]
        _ip = '127.0.0.1'
        global kernel_port
        _port = kernel_port
        global tk
        _token = tk
        context = {
            "message": "Hi! Welcome to JdeRobot Academy Web!",
            "exercises_list": exercises_list,
            "logout": True,
            "port": _port,
            "ip_address": _ip,
            "token": _token,
            "session": kernel_session,
        }

    return render(request, 'remoteAcademy/main_page.html', context)


# ==============================================================================
# ============================ EXERCISE SIMULATION =============================
# ==============================================================================


def local(request):
    """ Página de Simulación Local de un ejercicio """
    # Direccion IP del cliente
    client_ip = get_client_ip(request)
    print "Client ip: "+client_ip
    _ip = '127.0.0.1'
    # Recoger del formulario el puerto y el token del Notebook Server
    _port = request.POST['port']
    _token = request.POST['token']
    global tk
    tk = _token
    global kernel_port
    kernel_port = _port
    # URL del Notebook Server
    src = 'https://'+_ip+':'+_port+'/tree?token='+_token
    print "JUPYTER NOTEBOOK SERVER URL: " + src

    # Coger Notebook de la base de datos y convertir a JSON
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with io.open(os.path.join(__location__+'/static/remoteAcademy/backend/independiente', 'color_filter_indepe.ipynb'), 'r', encoding='utf8') as f:
        nbcontent = f.read()

    ### Enviar los ficheros de back-end del ejercicio ###
    # Localizar fichero en la base de datos
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with io.open(os.path.join(__location__+'/static/remoteAcademy/backend/independiente', 'color_filter.py'), 'r', encoding='utf8') as f:
    #with io.open(os.path.join(__location__+'/static/remoteAcademy/backend/independiente/pyarmor', src), 'r', encoding='utf8') as f:
        codefile = f.read()
    # Convertir fichero a objeto JSON
    codefile = json.dumps(codefile, indent = 2, encoding="utf8")
     # Localizar fichero en la base de datos
    with io.open(os.path.join(__location__+'/static/remoteAcademy/backend/independiente', 'color_filter_conf.yml'), 'r', encoding='utf8') as f:
    #with io.open(os.path.join(__location__+'/static/remoteAcademy/backend/independiente/pyarmor', src), 'r', encoding='utf8') as f:
        configfile = f.read()
    # Convertir fichero a objeto JSON
    configfile = json.dumps(configfile, indent = 2, encoding="utf8")

    context = {
        "src": src,
        "port": _port,
        "ip_address": _ip,
        "token": _token,
        "notebook": nbcontent,
        "codefile": codefile,
        "configfile": configfile,
        "simulation_site": True,
        "authenticate": True,
        "simulation_type" : "local",
    }
    return render(request, 'remoteAcademy/local.html', context)
