import requests
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
webpage = "https://getvideo.at/en/"
wvideo= input('Please Enter the Wvideo Code: ')
title= input('What would you like to name the video: ')
searchterm = "https://fast.wistia.net/embed/iframe/" + wvideo
d.get('https://getvideo.at/en/')
sbox = d.find_element_by_class_name("form-control")
sbox.send_keys(searchterm)
sbox.send_keys(Keys.ENTER)


try:
    listgroup= WebDriverWait(d, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "list-group"))
    )
    links=listgroup.find_elements_by_tag_name("a")
    extract_link=list()
    for link in links:
        href=link.get_attribute('href')
        extract_link.append(href)
    link_720=extract_link[3]
    print ("Downloading file:%s"%title)
    r = requests.get(link_720, stream = True)
    with open(title, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)
    print ("%s downloaded!\n"%title)
                
except Exception as e:
    print(e)




            
