from google_images_download import GoogleImagesDownload

def main(keywords):
    if len(keywords) > 0:
        response = GoogleImagesDownload()

        for keyword in keywords:
            response.download(keyword)

keywords = []

main(keywords)
