from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

import urllib.request

def google_images_download(keyword):
  driver = webdriver.Chrome("/Users/we/python-study/chromedriver")

  driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

  elem = driver.find_element_by_name("q")

  elem.send_keys(keyword)

  elem.send_keys(Keys.RETURN)

  SCROLL_PAUSE_TIME = 1.5

  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
      try:
        driver.find_element_by_css_selector(".mye4qd").click()
      except:
        break

    last_height = new_height

  images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

  count = 1

  for image in images:
    try:
      image.click()

      time.sleep(2)

      imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")

      urllib.request.urlretrieve(imgUrl, "download/" + keyword + "/"
      +
      str(count)
      +
      ".jpg")

      count = count + 1
    except:
      pass

  driver.close()
