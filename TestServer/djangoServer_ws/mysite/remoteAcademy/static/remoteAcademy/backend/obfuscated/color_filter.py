#!/usr/bin/env python
# -*- coding: utf-8 -*-
k=SystemExit
d=open
import sys
Q=sys.path
Q.append('/usr/lib/python2.7/')
import types
h=types.MethodType
import time
import cv2
import numpy as np
from MyAlgorithm import MyAlgorithm
import config
F=config.load
import comm
i=comm.init
import yaml
V=yaml.safe_load
c=yaml.YAMLError
from threadcamera import ThreadCamera
from cameraFilter import CameraFilter
from IPython.display import clear_output as S
def r(O):
 X=O['Introrob']['Source']
 if X.lower()=='local':
  from local_camera import Camera
  w=O['Introrob']['Local']['DeviceNo']
  print('  Chosen source: local camera (index %d)'%(w))
  u=Camera(w)
 elif X.lower()=='video':
  from local_video import Camera
  e=O['Introrob']['Video']['Path']
  print('  Chosen source: local video (%s)'%(e))
  u=Camera(e)
 elif X.lower()=='stream':
  import comm
  i=comm.init
  import config
  F=config.load
  O=F('color_filter_conf.yml')
  G=i(O,'Introrob')
  l=G.getCameraClient('Introrob.Stream')
  from stream_camera import Camera
  u=Camera(l)
 else:
  raise k(('%s not supported! Supported source: Local, Video, Stream')%(X))
 return u
def b():
 try:
  with d('color_filter_conf.yml','r')as stream:
   return V(stream)
 except c as exc:
  print(exc)
  raise k('Error: Cannot read/parse YML file. Check YAML syntax.')
 except:
  raise k('\n\tFILE "color_filter_conf.yml" DOES NOT EXIST\n')
class t():
 def __init__(L):
  O=b()
  L.camera=r(O)
  j=ThreadCamera(L.camera)
  j.start()
  L.algorithm=MyAlgorithm(L.camera)
  print "Color filter initialized OK"
 def g(L):
  L.algorithm.play()
  print "Color filter is running"
 def K(L):
  L.algorithm.pause()
  print "Color filter has been paused"
 def W(L):
  L.algorithm.stop()
  print "Color filter stopped"
 def n(L,ex):
  L.algorithm.func=ex
  def y(L):
   L.func(L)
   if(L.visualizationIterator%15)==0 and L.visualizationEnabled:
    if L.filtered_image.any():
     S()
     L.displaybuttons()
     L.printFilteredImage()
    else:
     print
     print "//////////////////////////////////// "
     print "You haven't set any Filtered Image!!"
     print "//////////////////////////////////// "
     print
  L.algorithm.algorithm=h(y,L.algorithm)
  print "Code updated"
 def R(L):
  return L.algorithm.get_filtered_image()
 def B(L):
  return L.algorithm.get_color_image()
