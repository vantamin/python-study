import os

from urllib.parse import urlparse

def get(url):
    url = urlparse(url)

    return os.path.basename(url.path)
