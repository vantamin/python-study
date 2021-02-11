from google_images_crop import GoogleImagesCrop

def main(keywords):
    if len(keywords) > 0:
        response = GoogleImagesCrop()

        for keyword in keywords:
            response.download(keyword, 100)

keywords = []

main(keywords)
