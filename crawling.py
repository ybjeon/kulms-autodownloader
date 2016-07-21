#!flask/bin/python
#! -*- coding:utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import config
from selenium.webdriver.common.keys import Keys

login_url = 'https://kulms.korea.ac.kr/'
base_url = 'https://kulms.korea.ac.kr/webapps/gradebook/do/instructor/viewNeedsGrading?sortDir=ASCENDING&sortCol=attemptDate&numResults=25&course_id=_64035_1&pageIndex='
file_path = '/home/jeonyoungbae/dev/downloadTA/files'

def getURL(num):
    return base_url+str(num)

chromeoptions = webdriver.ChromeOptions()

prefs = {'download.default_directory': file_path}
chromeoptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeoptions)
driver.get(login_url)

field = driver.find_element_by_id('loginFormFields')
user_id = driver.find_element_by_name('user_id')
user_id.send_keys(config.id)
user_pw = driver.find_element_by_name('password')
user_pw.send_keys(config.pw)
user_pw.send_keys(Keys.ENTER)

idx = 0
while True:
    try:
        driver.get(getURL(idx))
        item = driver.find_element_by_id('controlpanel.grade.center_groupContents')

        break
        items = driver.find_element_by_id('listContainer_databody')
        items = items.find_elements_by_tag_name('tr')
        item_folder = ''
        item_user = ''
        total_num = len(items)
        for i in range(total_num):
            items = driver.find_element_by_id('listContainer_databody')
            items = items.find_elements_by_tag_name('tr')
            item = items[i]
            item_user =  item.find_element_by_class_name('gradeAttempt')
            item_folder =  item.find_elements_by_tag_name('td')[1]
            str_user = item_user.text
            str_folder = item_folder.text
            item_user.click()
            btns = driver.find_elements_by_class_name('dwnldBtn')
            for item in btns:
                item.click()
                print item.text
            driver.get(getURL(idx))
            #driver.execute_script('window.history.go(-1)')

        pages = driver.find_element_by_id('listContainer_itemcount')
        strongs =  pages.find_elements_by_tag_name('strong')
        if strongs[1].text==strongs[2].text:
            print 'end page'
            break
        idx = idx+1
                #driver.get(base_url)
        #print driver.find_element_by_id('loginFormFields')
#        print ids[idx]
#        soup = bs(driver.page_source, 'html.parser')
#        body = soup.find('div', class_='vertical layout style-scope search-result')
#        box = body.find('div',class_='flex-2 style-scope search-result')
#        datebox = box.find('dl', class_='key-dates style-scope search-app')
#        data['title'] = body.find('h1', class_='style-scope search-app').text
#        print '[title]', data['title']
#        data['abstract'] = body.find('div', class_='abstract style-scope patent-text').text
#        print '[abstract]', data['abstract']
#        dates = datebox.find_all('dt', class_='style-scope search-app')
#        dates_text = datebox.find_all('dd', class_='style-scope search-app')
#        dates_exist = []
#        for n, item in enumerate(dates):
#            text = item.text.strip()
#            if text == 'Filing date':
#                data['filing_date']=dates_text[n].text.strip()
#                print text, data['filing_date']
#            elif text == 'Publication date':
#                data['publication_date']=dates_text[n].text.strip()
#                print text, data['publication_date']
#            elif text == 'Grant date':
#                data['grant_date']=dates_text[n].text.strip()
#                print text, data['grant_date']
#            elif text == 'Priority date':
#                data['priority_date']=dates_text[n].text.strip()
#                print text, data['priority_date']
#
#        footer = body.find('div', class_='footer style-scope search-app')
#        footer_list = footer.find_all('h3')
#        for n, item in enumerate(footer_list):
#            text = item['id'].strip()
#            table = body.find_all('table', class_='style-scope search-app')[n]
#            if text == 'similarDocuments':
#                print '=similar'
#                arr = table.find_all('tr', class_='style-scope search-app')
#                for m,row in enumerate(arr):
#                    if m>0:
#                        print str(row.text).split()[0]
#                        db.session.add(db.Similar(
#                        id=ids[idx],
#                        similar_id=str(row.text).split()[0]))
#                        db.session.commit()
#            elif text == 'legalEvents':
#                print '=legalEvents'
#                arr = table.find_all('tr', class_='style-scope search-app')
#                for m,row in enumerate(arr):
#                    try:
#                        arr=row.find_all('td')
#                        data['legal_events'] = {'date':arr[0].text,'code':arr[1].text,'title':arr[2].text}
#                        print arr[0].text, arr[1].text, arr[2].text
#                    except AttributeError as e:
#                        print e.message
#                    except IndexError as e:
#                        print e.message

#                    if m>0:
#                        string = row.text.split()
#                        for item2 in string:
#                            if item2 == '*':
#                                string.remove(item2)
#                        print string[0], string[1], string[2], string[3]
#            elif text == 'citedBy':
#                print '=citedBy'
#                arr = table.find_all('tr', class_='style-scope search-app')
#                for m,row in enumerate(arr):
#                    if m>0:
#                        print str(row.text).split()[0]
#                        db.session.add(db.Cited(
#                            id=ids[idx],
#                            citedby_id=str(row.text).split()[0]))
#                        db.session.commit()
#
#            try:
#                data['title']
#            except KeyError as e:
#                data['title']=''
#            try:
#                data['abstract']
#            except KeyError as e:
#                data['abstract']=''
#            try:
#                data['filing_date']
#            except KeyError as e:
#                data['filing_date']=''
#            try:
#                data['priority_date']
#            except KeyError as e:
#                data['priority_date']=''
#            try:
#                data['publication_date']
#            except KeyError as e:
#                data['publication_date']=''
#            try:
#                data['legal_events']
#            except KeyError as e:
#                data['legal_events']={}
#
#            if not db.is_exist(db.Data, ids[idx]):
#                db.session.add(db.Data(id=ids[idx],
#                                   title=data['title'],
#                                   abstract=data['abstract'],
#                                   filling_date=data['filing_date'],
#                                   priority_date=data['priority_date'],
#                                   publication_date=data['publication_date'],
#                                   legal_events=str(data['legal_events'])
#                                   ))
#                db.session.commit()
    except AttributeError as e:
        print e.message
#    except IndexError as e:
#        print e.message
#    except UnicodeError as e:
#        print e.message
    finally:
        idx+=1
