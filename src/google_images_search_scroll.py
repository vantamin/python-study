from google_images_search import GoogleImagesSearch

import time

class GoogleImagesSearchScroll(GoogleImagesSearch):
    SCROLL_PAUSE_TIME = 1.5

    def pause(self):
        time.sleep(self.SCROLL_PAUSE_TIME)

    def scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight;")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            self.pause()

            new_height = self.driver.execute_script("return document.body.scrollHeight;")

            if new_height == last_height:
                try:
                    self.driver.find_element_by_css_selector(".mye4qd").click()
                except:
                    break

            last_height = new_height

    def search(self):
        super().search()

        self.scroll()
