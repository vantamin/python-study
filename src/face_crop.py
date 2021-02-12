from urllib.request import urlopen

import numpy as np

import cv2

face_cascade = cv2.CascadeClassifier("lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml")

eyes_cascade = cv2.CascadeClassifier("lib/python3.8/site-packages/cv2/data/haarcascade_eye.xml")

def face_crop(url, filename):
    retval = urlopen(url)

    dst = np.asarray(bytearray(retval.read()), dtype="uint8")

    dst = cv2.imdecode(dst, cv2.COLOR_BGR2GRAY)

    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(dst, 1.3, 5)

    i = 1

    for x, y, w, h in faces:
        img = dst[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]

        cv2.imwrite(filename + "_" + str(i) + ".jpg", img)

        i = i + 1
