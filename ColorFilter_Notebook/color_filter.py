#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/lib/python2.7/')
import types
import yaml

from os import path
import traceback
import threading
import time
from datetime import datetime

import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

class Camera:

    def getImage(self):
        ''' Gets the image from the webcam and returns it. '''
        return self.image

    def update(self):
        ''' Updates the camera with a frame from the device every time the thread changes. '''
        if self.cam:
            self.lock.acquire()
            _, frame = self.cam.read()
            self.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.lock.release()

    def getColorImage(self):
        img = np.zeros((self.height, self.width,3), np.uint8)
        img = self.trackImage
        img.shape = self.trackImage.shape
        return img

    def setColorImage(self,image):
        self.trackImage = image
        self.trackImage.shape = image.shape

    def getThresholdImage(self):
        img = np.zeros((self.height, self.width,1), np.uint8)
        img = self.thresholdImage
        img.shape = self.thresholdImage.shape
        return img

    def setThresholdImage(self,image):
        self.thresholdImage = image
        self.thresholdImage.shape = image.shape

class ThreadCamera(threading.Thread):

    def __init__(self, cam):
        ''' Threading class for Camera. '''

        self.t_cycle = 50      # ms

        self.cam = cam
        threading.Thread.__init__(self)

    def run(self):
        ''' Updates the thread. '''
        while(True):
            start_time = datetime.now()
            self.cam.update()
            end_time = datetime.now()

            dt = end_time - start_time
            dtms = ((dt.days * 24 * 60 * 60 + dt.seconds) * 1000
                + dt.microseconds / 1000.0)

            delta = max(self.t_cycle, dtms)
            self.framerate = int(1000.0 / delta)

            if(dtms < self.t_cycle):
                time.sleep((self.t_cycle - dtms) / 1000.0)

class LocalCamera(Camera):

    def __init__ (self, device_idx):
        ''' Camera class gets images from a video device and transform them
        in order to detect objects in the image.
        '''
        self.lock = threading.Lock()
        self.cam = cv2.VideoCapture(device_idx)
        
        if not self.cam.isOpened():
            print("%d is not a valid device index in this machine." % (device_idx))
            raise SystemExit("Please check your camera id (hint: ls /dev)")

        self.width = int(self.cam.get(3))
        self.height = int(self.cam.get(4))
        self.image = np.zeros((self.height, self.width,3), np.uint8)
        
        self.trackImage = np.zeros((self.height, self.width,3), np.uint8)
        self.trackImage.shape = self.height, self.width, 3

        self.thresholdImage = np.zeros((self.height,self. width,1), np.uint8)
        self.thresholdImage.shape = self.height, self.width,


class LocalVideo(Camera):

    def __init__ (self, video_path):
        ''' Camera class gets images from a video device and transform them
        in order to detect objects in the image.
        '''
        self.lock = threading.Lock()
        video_path = path.expanduser(video_path)

        if not path.isfile(video_path):
            raise SystemExit('%s does not exists. Please check the path.' % (video_path))

        self.cam = cv2.VideoCapture(video_path)
        if not self.cam.isOpened():
            print("%d is not a valid device index in this machine." % (device_idx))
            raise SystemExit("Please check your camera id (hint: ls /dev)")

        self.width = self.cam.get(3)
        self.height = self.cam.get(4)
        self.image = np.zeros((self.height, self.width,3), np.uint8)

        self.trackImage = np.zeros((self.height, self.width,3), np.uint8)
        self.trackImage.shape = self.height, self.width, 3

        self.thresholdImage = np.zeros((self.height,self. width,1), np.uint8)
        self.thresholdImage.shape = self.height, self.width,


def selectVideoSource(cfg):
    """
    @param cfg: configuration
    @return cam: selected camera
    @raise SystemExit in case of unsupported video source
    """
    source = cfg['Introrob']['Source']
    if source.lower() == 'local':
        #from local_camera import Camera
        cam_idx = cfg['Introrob']['Local']['DeviceNo']
        print('  Chosen source: local camera (index %d)' % (cam_idx))
        cam = LocalCamera(cam_idx)
    elif source.lower() == 'video':
        #from local_video import Camera
        video_path = cfg['Introrob']['Video']['Path']
        print('  Chosen source: local video (%s)' % (video_path))
        cam = LocalVideo(video_path)
    #elif source.lower() == 'stream':
        # comm already prints the source technology (ICE/ROS)
        #import comm
        #import config
        #cfg = loadConfig('color_filter_conf.yml')
        #jdrc = comm.init(cfg, 'Introrob')
        #proxy = jdrc.getCameraClient('Introrob.Stream')
        #from stream_camera import Camera
        #cam = Camera(proxy)
    else:
        raise SystemExit(('%s not supported! Supported source: Local, Video, Stream') % (source))

    return cam


def readConfig():
    try:
        with open('color_filter_conf.yml', 'r') as stream:
            return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        raise SystemExit('Error: Cannot read/parse YML file. Check YAML syntax.')
    except:
        raise SystemExit('\n\tFILE "color_filter_conf.yml" DOES NOT EXIST\n')

class ColorFilter ():

    def __init__(self):

        cfg = readConfig()
        self.camera = selectVideoSource(cfg)
        # Threading the camera...
        t_cam = ThreadCamera(self.camera)
        t_cam.start()

        self.algorithm = MyAlgorithm(self.camera)
        
        print "Color filter initialized OK"
        
    def play(self):
        # self.unpause_physics_client()
        self.algorithm.play()
        print "Color filter is running"
        
    def pause (self):
        self.algorithm.pause()
        #self.pause_physics_client()
        print "Color filter has been paused"
         
    def stop(self):
        self.algorithm.stop()
        print "Color filter stopped"
                   
    def setExecute(self, ex):
        self.algorithm.func = ex
        def execute(self):
            self.func(self)
            # print filtered image each 30 interations
            if (self.visualizationIterator % 15) == 0 and self.visualizationEnabled:
                if self.filtered_image.any():
                    clear_output()
                    self.displaybuttons()
                    self.printFilteredImage()
                else:
                    print
                    print "//////////////////////////////////// "
                    print "You haven't set any Filtered Image!!"
                    print "//////////////////////////////////// "
                    print

        self.algorithm.algorithm = types.MethodType(execute, self.algorithm)
        print "Code updated"       
        
    def get_filtered_image (self):
        return self.algorithm.get_filtered_image()
    
    def get_color_image (self):
        return self.algorithm.get_color_image()

def printImage(image):
    plt.axis('off')
    a = plt.imshow(image)
    plt.show()

def printVideo(image):
    #plt.close()
    plt.axis('off')
    v = plt.imshow(image)
    plt.show()
    time.sleep(2)
    plt.close()

time_cycle = 80
class MyAlgorithm(threading.Thread):

    def __init__(self, camera=None):
        self.camera = camera
        self.started = False
        self.func = None
        
        self.filtered_image = np.zeros((480,640,3), np.uint8)
        self.color_image = np.zeros((480,640,3), np.uint8)
        self.visualizationIterator = 0
        self.visualizationEnabled = False

        self.stop_event = threading.Event()
        self.stop_event.set()
        self.kill_event = threading.Event()
        self.lock = threading.Lock()
        self.filtered_image_lock = threading.Lock()
        self.color_image_lock = threading.Lock()
        threading.Thread.__init__(self, args=self.stop_event)

    def run (self):

        while (not self.kill_event.is_set()):

            self.stop_event.wait()
            
            start_time = datetime.now()

            self.algorithm()
            self.visualizationIterator += 1    

            finish_Time = datetime.now()

            dt = finish_Time - start_time
            ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
            
            if (ms < time_cycle):
                time.sleep((time_cycle - ms) / 1000.0)

    def pause (self):
        # Academic Pause
        self.stop_event.clear()
        
    def play (self):
        self.stop_event.set()
        if not self.started:
          self.start()
          self.started = True

    def stop (self):
        self.kill_event.set()
        
    def set_color_image (self, image):
        img  = np.copy(image)
        if len(img.shape) == 2:
          img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        self.color_image_lock.acquire()
        self.color_image = img
        self.color_image_lock.release()
        
    def get_color_image (self):
        self.color_image_lock.acquire()
        img = np.copy(self.color_image)
        self.color_image_lock.release()
        return img
        
    def set_filtered_image (self, image):
        img = np.copy(image)
        if len(img.shape) == 2:
          img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        self.filtered_image_lock.acquire()
        self.filtered_image = img
        self.filtered_image_lock.release()
        
    def get_filtered_image (self):
        self.filtered_image_lock.acquire()
        img  = np.copy(self.filtered_image)
        self.filtered_image_lock.release()
        return img

    def printFilteredImage(self):
        printImage(self.filtered_image)

    def algorithm(self):
        if (self.visualizationIterator % 15) == 0 and self.visualizationEnabled:
            if self.filtered_image.any():
                clear_output()
                self.printFilteredImage()
            else:
                    print
                    print "//////////////////////////////////// "
                    print "You haven't set any Filtered Image!!"
                    print "//////////////////////////////////// "
                    print
        
