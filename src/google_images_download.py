from google_images_search_scroll import GoogleImagesSearchScroll

from utils import download_file, split_path

from tkinter import filedialog

import os

class GoogleImagesDownload(GoogleImagesSearchScroll):
    def __init__(self):
        self.dirname = filedialog.askdirectory()

    def set_download(self, url, filename):
        download_file.download(url, filename)

    def download(self, keyword, limit=False):
        if False if self.dirname else True:
            return

        self.search(keyword)

        images = self.driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

        path = self.dirname + "/" + keyword

        try:
            os.mkdir(path)
        except:
            pass

        index = 1

        count = 1

        for image in images:
            if limit:
                if count > limit:
                    break

            try:
                image.click()

                self.pause()

                url = self.driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")

                filename = split_path.get(url)

                if len(filename.split(".")) == 1:
                    filename = filename + ".jpg"

                filename = str(index).zfill(3) + "_" + filename

                self.set_download(url, os.path.join(path, filename))

                count = count + 1
            except:
                pass

            index = index + 1

        self.close()
