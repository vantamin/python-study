from tkinter import filedialog

from face_crop import face_crop

import os

path = filedialog.askdirectory()

dirs = os.listdir(path)

try:
    os.mkdir("download")
except:
    pass

for dir in dirs:
    if dir == ".DS_Store":
        continue

    try:
        os.mkdir("download/" + dir)
    except:
        pass

    files = os.listdir(path + "/" + dir)

    for file in files:
        if dir == ".DS_Store":
            continue

        url = path + "/" + dir + "/" + file

        filename = file.replace(".JPG", "").replace(".jpg", "").replace(".jpeg", "").replace(".png", "")

        filename = "download/" + dir + "/" + filename

        try:
            face_crop(url, filename)
        except:
            pass
