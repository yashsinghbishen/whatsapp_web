import selenium
from selenium import webdriver
import time

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=E:\\Whatsapp_automation\\project_whatsapp\\chrome_data")
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
users = ['Raju Rki']
time.sleep(40)
for user in users:
    msg = '''
    HI {} 
    This is sample test no need to reply.
    Some automation stuff nothing else.
        '''.format(str(user))
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(user))
    user.click()
    #  copyable-text selectable-text
    # <div class="_3u328 copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div>
    msg_box = driver.find_element_by_class_name(['_3FeAD','_1PRhq']).click()
    msg_box = driver.find_element_by_xpath('copyable-text')
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('compose-btn-send').click()
time.sleep(50000)