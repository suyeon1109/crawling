# -*- coding: utf-8 -*-
# parser.py


from socket import AI_PASSIVE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def createDirectory(directory):
    try: 
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to created the directory")

def crawling_img(name):
    driver = webdriver.Chrome("/Users/mac/Documents/GitHub/crawling/chromedriver")
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
    elem = driver.find_element_by_name('q') #서치바의 태그
    elem.send_keys(name) #태연
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME=1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height
    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    dir = "/Users/mac/Documents/GitHub/crawling/"+name
    createDirectory(dir)

    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            path = dir + '/'
            urllib.request.urlretrieve(imgUrl, path+name+str(count)+".jpg")
            count+=1

            if count >=10:
                break
        except:
            pass
    driver.close()


crawling_img("지코")