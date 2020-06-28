import numpy as np
import cv2
import time


class cv_proxy():
    def __init__(self):
        self.model = {
            'timestamp': '',
            'image': ''
        }        
        self.cap = cv2.VideoCapture('video/20200606_072829.mp4')
        #self.cap = cv2.VideoCapture(0)
    def getpicture(self):
        ret, frame = self.cap.read()
        self.model['image'] = cv2.imencode('.jpg', frame)[1].tostring()
        localtime = time.gmtime((int(time.time()) + 28800))
        self.model['timestamp'] = int(time.time()) + 28800
        localtime_str = time.strftime('%Y:%m:%d %H:%M:%S', localtime)
        print('------------------------------')
        print('record image: ' + localtime_str)
        cv2.imwrite(f"{self.model['timestamp']}.jpg", frame)
        return self.model
        
    def __del__(self):
        self.cap.release()
