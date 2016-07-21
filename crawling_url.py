#!-*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pickle_trace as pt
import time

pt.load_trace('id_iotsecurity.txt')

driver = webdriver.Firefox()
idx=1
while True:
    driver.get("https://patents.google.com/?q=\"IoT\"+security&language=ENGLISH&country=DE&page="+str(idx))
    cnt=0
    while True:
        soup = bs(driver.page_source, 'html.parser')
        arr = soup.find_all('a', class_='result-title style-scope search-result-item')
        if len(arr) is 0:
            print "wait for : ", 20-cnt
            cnt=cnt+1
            if cnt>20:
                exit()
            time.sleep(1)
            continue
        print 'page : ', idx
        for item in arr:
            id =item.get('href').split('/')[2]
            if not pt.check_id(id):
                print id
                pt.add_id(id)
            else:
                print 'pass'
        idx=idx+1
        break
