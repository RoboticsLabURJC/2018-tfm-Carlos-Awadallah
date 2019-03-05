# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.conf import settings
import urllib2
import json
import io
import os

#exercises_location = settings.BASE_DIR + "/exercises"
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
    print x_forwarded_for
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
    """ Página principal de la Aplicación """

    cf = Exercise('Color Filter', 'portfolio_color_filter.png')
    exercises_list = [cf]
    context = {
        "message": "Hi! Welcome to JdeRobot Academy Web!",
        "exercises_list": exercises_list,
    }
    return render(request, 'remoteAcademy/main_page.html', context)

def del_code(ip,port,token,src):
    # Eliminar un fichero
    src_del='http://'+ip+':'+port+'/api/contents/'+src
    request_jupyter_del = urllib2.Request(src_del, data="")
    request_jupyter_del.add_header('Authorization', 'token ' + token)
    request_jupyter_del.get_method = lambda: 'DELETE'
    res = urllib2.urlopen(request_jupyter_del)
    content = res.read()
    print content

def logout(request):
    """ Vista de logout. Redirecciona a la página principal """
    # Direccion IP del cliente
    _ip = get_client_ip(request)

    # Recoger Notebook relleno
    global kernel_port
    src_notebook='http://'+_ip+':'+kernel_port+'/api/contents/color_filter.ipynb'
    request_jupyter_get = urllib2.Request(src_notebook, data="")
    global tk
    request_jupyter_get.add_header('Authorization', 'token ' + tk)
    request_jupyter_get.get_method = lambda: 'GET'
    res = urllib2.urlopen(request_jupyter_get)
    #print res
    content = res.read()
    message_info = json.loads(content)
    new_notebook= {}
    new_notebook = message_info['content']

    # Guardar el Notebook Relleno en el servidor web
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'color_filter.ipynb'), 'w') as nb:
        json.dump(new_notebook, nb)
    nb.close()

    # Eliminar Session y KernelL
    global session
    src_session='http://'+_ip+':'+kernel_port+'/api/sessions/'+session
    request_jupyter_del = urllib2.Request(src_session, data="")
    global tk
    request_jupyter_del.add_header('Authorization', 'token ' + tk)
    request_jupyter_del.get_method = lambda: 'DELETE'
    res = urllib2.urlopen(request_jupyter_del)
    content2 = res.read()
    #print content

    # Lista de ficheros a eliminar
    code_files = ['cameraFilter.py','threadcamera.py','local_camera.py','local_video.py','stream_camera.py','color_filter.py',
                  'MyAlgorithm.py','printer.py','cameraserver_conf.cfg','color_filter_conf.yml','color_filter.ipynb']
    #code_files_obfuscated = ['color_filter.py','color_filter.ipynb', 'pytransform.py','pytransform.key']
    # Eliminar ficheros de back-end del ejercicio
    for i in range(0,2):
        if i == 0:
            for f in code_files:
                del_code(_ip,kernel_port,tk,f) 
                print "DELETED "+f
        else:    
            for f in code_files:
                if f[-2:] == 'py':
                    f = f[:-2]+'pyc'
                    try:
                        del_code(_ip,kernel_port,tk,f)
                        print "DELETED "+f
                    except:
                        print f+' NOT FOUND'
    

    return redirect('exercises')

# ==============================================================================
# ============================ EXERCISE SIMULATION =============================
# ==============================================================================

def send_code(ip,port,token,src):
    
    # Localizar fichero en la base de datos
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with io.open(os.path.join(__location__+'/static/remoteAcademy/backend', src), 'r', encoding='utf8') as f:
    #with io.open(os.path.join(__location__+'/static/remoteAcademy/backend/independiente/pyarmor', src), 'r', encoding='utf8') as f:
        codefile = f.read()
    
    # Convertir fichero a objeto JSON
    codefile = json.dumps(codefile, indent = 2, encoding="utf8")

    src_code = 'http://'+ip+':'+port+'/api/contents/'+src
    data_put = ' {"type": "file","format": "text","content": ' + codefile + '} '
    request_jupyter = urllib2.Request(src_code, data=data_put)
    request_jupyter.add_header('Content-Type', 'application/json')
    request_jupyter.add_header('Authorization', 'token ' + token)
    request_jupyter.get_method = lambda: 'PUT'
    res = urllib2.urlopen(request_jupyter)
    content = res.read()
    #print content
    print "CODEFILE COPIED "+src

def local(request):
    """ Página de Simulación Local de un ejercicio """
    # Direccion IP del cliente
    _ip = get_client_ip(request)
    print "Client ip: "+_ip
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

    # Solicitar Cookie
    '''request_1 = urllib2.Request('http://127.0.0.1:8888/tree', data='{}')
    #request_jupyter.add_header('Content-Type', 'application/json')
    #request_jupyter.add_header('Authorization', 'token ' + _token)
    request_1.get_method = lambda: 'GET'
    res_1 = urllib2.urlopen(request_1)
    content_1 = res_1.read()
    print res_1.info()['Set-Cookie'][6:-8]
    cookies = request.COOKIES
    print cookies
    cookies['_xsrf'] = res_1.info()['Set-Cookie'][6:-8]
    print cookies'''

    # Coger Notebook de la base de datos y convertir a JSON
    src_nb = 'http://'+_ip+':'+_port+'/api/contents/color_filter.ipynb'
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with io.open(os.path.join(__location__, 'color_filter.ipynb'), 'r', encoding='utf8') as f:
        nbcontent = f.read()

    # Copiar Notebook en /api/contents/
    data_put = ' {"type": "notebook","format": "json","content": ' + nbcontent + '} '
    request_jupyter = urllib2.Request(src_nb, data=data_put)
    request_jupyter.add_header('Content-Type', 'application/json')
    request_jupyter.add_header('Authorization', 'token ' + _token)
    #request_jupyter.add_header('X-XSRFToken', res_1.info()['Set-Cookie'][6:-8])
    request_jupyter.get_method = lambda: 'PUT'
    res = urllib2.urlopen(request_jupyter)
    #content = res.read()
    #print content
    print "---------------"
    print "NOTEBOOK COPIED"
    print "---------------"

    # Enviar los ficheros de back-end del ejercicio
    send_code(_ip,_port,_token,'threadcamera.py')
    send_code(_ip,_port,_token,'local_camera.py')
    send_code(_ip,_port,_token,'local_video.py')
    send_code(_ip,_port,_token,'stream_camera.py')
    send_code(_ip,_port,_token,'color_filter.py')
    send_code(_ip,_port,_token,'cameraFilter.py')
    send_code(_ip,_port,_token,'MyAlgorithm.py')
    send_code(_ip,_port,_token,'printer.py')
    send_code(_ip,_port,_token,'cameraserver_conf.cfg')
    send_code(_ip,_port,_token,'color_filter_conf.yml')

    '''send_code(_ip,_port,_token,'color_filter.py')
    send_code(_ip,_port,_token,'color_filter_conf.yml')
    send_code(_ip,_port,_token,'pytransform.py')
    send_code(_ip,_port,_token,'pytransform.key')'''

    #cookie_xsrf = request.COOKIES.get('_xsrf') 
    #cookie_pair = request.COOKIES.get('username-'+_ip+'-'+_port)
    #print cookie_xsrf

    # Iniciar Session y Kernel en el Notebook Server remoto
    src_session = 'http://'+_ip+':'+_port+'/api/sessions'
    data_session_post = '{"name":"color_filter.ipynb","path":"color_filter.ipynb","type": "notebook","kernel": {"name": "python2"}}'
    request_jupyter_post = urllib2.Request(src_session, data=data_session_post)
    request_jupyter_post.add_header('Content-Type', 'application/json')
    request_jupyter_post.add_header('Authorization', 'token ' + _token)
    request_jupyter_post.get_method = lambda: 'POST'
    res = urllib2.urlopen(request_jupyter_post)
    content = res.read()
    #print content
    message_info = json.loads(content)
    session_id = message_info['id']
    print "Current Jupyter Session: "+session_id
    global session
    session = session_id
    kernel_id = message_info['kernel']['id']
    print "Kernel ID: "+kernel_id
    print "---------------"
    print "KERNEL CREATED"
    print "---------------"

    context = {
        "src": src,
        "port": _port,
        "ip_address": _ip,
        "token": _token,
        "simulation_site": True,
        "authenticate": True,
        "simulation_type" : "local",
    }
    return render(request, 'remoteAcademy/local.html', context)
