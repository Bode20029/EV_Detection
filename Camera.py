import io
import os
import cv2
import pygame as pg
import time
from config import *

SECONDS_TO_DETECT = 5
starting_time = time.time()
timer_started = False
class Camera:
    def __init__(self, source):
        #Video Capture
        self.video = cv2.VideoCapture(source)
        self.soundFile = os.getcwd() + os.sep + 'car-honk.mp3'
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # Threshold to filter weak detections
                if not timer_started:
                
                    starting_time = True
                    timer_started = True
                    print("Timer started!")