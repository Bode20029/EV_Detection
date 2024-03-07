import io
import os
import cv2

class Camera:
    def __init__(self, source):
        #Video Capture
        self.video = cv2.VideoCapture(source)
        