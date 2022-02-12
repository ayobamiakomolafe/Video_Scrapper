import requests
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



dico={'Chapter 1 Module 1- What is Credit ': 'm9icn9oasl', 'Chapter 1 Module 2- What is a Credit Score Used For ': 'su49ar5pnt',
 'Chapter 1 Module 3- The Three Credit Bureaus ': 'a0apw717re', 'Chapter 1 Module 4- The 3 Major Credit Monitoring Services ': 'n7a3yxgdjy',
 'Chapter 1 Module 5- The Average Credit Card Debt ': 'lpb4mcuapy', 'Chapter 1 Module 6- How Your Score is Calculated ': 'a6xl0jrizp',
 'Chapter 1 Module 7- Understanding Your Score ': '4uu17mk6gy', 'Chapter 1 Module 8- Inquiries: Hard Pull vs Soft Pull ': '0il8qyii9l',
 'Chapter 2 Module 1- What is a Tradeline ': 'f816nvsupx', 'Chapter 2 Module 2- What is Credit Repair ': 'k928o0s7ad',
 'Chapter 2 Module 3- Business Tradelines vs Personal Tradelines ': 'egm2pgnhgd', 'Chapter 2 Module 4- Making Your Payments On Time ': 'iceui112lq',
 'Chapter 2 Module 5- Credit Utilization ': '4ihivt01hh', 'Chapter 2 Module 6- Not Applying Too Often ': 'yrjtp6896u', 'Chapter 2 Module 7- Filling Out Your Applications ': 'cmhdwy4d8f',
 'Chapter 2 Module 8- Checking Your Credit Report For Errors ': 'fwa9lgvbtc', 'Chapter 2 Module 9- Two Ways to Build Credit ': 't403nk1g1b',
 'Chapter 2 Module 10- What is a Co-Signer ': '1ufyct02ya', 'Chapter 3 Module 1- Mistakes Can Be Made ': 'p11vh0w5gs', 'Chapter 3 Module 2- Inaccurate Information ': 'j5u91ilhw7',
 'Chapter 3 Module 3- Less Impact ': 'd587yn3zr5', 'Chapter 3 Module 4- More Impact ': 'vqkbu8ma44', "Chapter 3 Module 5- Things You Don't Need to Worry About ": '1l9mvsmd3t',
 'Chapter 3 Module 6- What to Do With The Negatives ': '3ja89ropco', 'Chapter 3 Module 7- The Investigation Begins ': '1q6dt4wo09',
 'Chapter 4 Module 1- Raising Your Credit Score ': 'gqkamn7jh9', 'Chapter 4 Module 2- Need a Few Extra Points ': 'odwkxf3qyx',
 'Chapter 4 Module 3- Do Not Close Unused Accounts ': 'gnvhp3zpmi', 'Chapter 4 Module 4 - Balancing Act ': 'sc4es2quic',
 'Chapter 4 Module 5- Little Known Secret ': 's79lepd22j', 'Chapter 4 Module 6- Little Known Secret Part 2 ': '935m03aiq6', "Chapter 4 Module 7- Start Early Don't Wait ": 'ott3e87y69',
 'Chapter 5 Module 1- Credit Repair ': '8qmwgp03dv', 'Chapter 5 Module 2- Inquiry Removal ': 'rk3xq4hq3q', 'Chapter 5 Module 3- Tradelines ': 'yd9ulpf3qm',
 'Chapter 5 Module 4 - LexisNexis ': '31gjervu8k', 'Chapter 5 Module 5- Debt Consolidation ': 'j0vrup3kzz', 'Chapter 5 Module 6- Credit Counseling ': 'pnyrtpo9cc',
 'Chapter 5 Module 7- Funding Companies ': '51phrzl3hc', 'The Live Call ': 'ejcd0pcsq3', 'Growing Your List ': 'iiu13jbbja',
 'The Follow Up ': '7572hxl8xn', 'Social Media Marketing, Google Adwords, and Email Newsletter ': 'rlb7bibc8p',
 'Intro ': '5a7e786lmj', '2 Sales 101 A ': 'pm359h29r2', 'How to Select the Right Tradelines ': 'evyb25vj9n'}

d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

webpage = "https://getvideo.at/en/"
download_links=dict()
for title,wvideo in dico.items():
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
        download_links[title]=link_720
        print ("Downloading file:%s"%title)
        r = requests.get(link_720, stream = True)
        with open(title, 'wb') as f:
          for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
              f.write(chunk)
        print ("%s downloaded!\n"%title)
    except Exception as e:
        print(e)
        continue
print ("All videos downloaded!")

data_items = download_links.items()
data_list = list(data_items)
df = pd.DataFrame(data_list)
df.to_csv('downloaded_files.csv')






