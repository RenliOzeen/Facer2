import cv2
import numpy as np
from PIL import Image
import os

def counter():
    path='dataset'

    detector = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml");
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]   

    if len(os.listdir(path))==0:
        id=0
    else:
        faceSamples=[]
        ids = []


        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)


        id=len(faces)+1
        return id

