from google_images_download import GoogleImagesDownload

from face_crop import face_crop

class GoogleImagesCrop(GoogleImagesDownload):
    def set_download(self, url, filename):
        face_crop(url, filename)
