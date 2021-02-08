import cv2

face_cascade = cv2.CascadeClassifier("lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml")

eyes_cascade = cv2.CascadeClassifier("lib/python3.8/site-packages/cv2/data/haarcascade_eye.xml")

def face_crop(url, filename):
    retval = cv2.imread(url)

    dst = cv2.cvtColor(retval, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(dst, 1.3, 5)

    i = 1

    for x, y, w, h in faces:
        img = retval[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]

        cv2.imwrite(filename + str(i) + ".jpg", img)

        i = i + 1
