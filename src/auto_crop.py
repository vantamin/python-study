from PIL import Image

from autocrop import Cropper

def auto_crop(url, filename):
    cropper = Cropper()

    cropped_array = cropper.crop(url)

    cropped_image = Image.fromarray(cropped_array)

    cropped_image.save(filename)
