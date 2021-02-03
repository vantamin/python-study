from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class GoogleImagesSearch:
    def search(self, keyowrd):
        self.driver = webdriver.Chrome("src/chromedriver")

        self.driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

        elem = self.driver.find_element_by_name("q")

        elem.clear()

        elem.send_keys(keyowrd)

        elem.send_keys(Keys.RETURN)

    def close(self):
        self.driver.close()
