import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os


chrome_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "chrome_data"
)
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + chrome_dir)
driver = webdriver.Chrome(options=options)
try:
    driver.get("http://127.0.0.1:5000/")
    users = ["Abhi", "Raju Rki", "Web Aspirant", "Sarvesh Tiwari", "Sweetest Sister"]
    # time.sleep(40)
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="side"]/header/div[2]/div/span/div[3]/div[@title="Menu"]',
            )
        )
    )
    for user in users:
        msg = """
        HI {} This is sample test no need to reply. Some automation stuff nothing else.
        """.format(
            str(user)
        )
        try:
            user1 = driver.find_element(
                By.XPATH,
                '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]/span/span[@title="{}"]'.format(
                    user
                ),
            )
        except:
            print('{} not found in your contect list'.format(user))
        # user1 = driver.find_elements(
        #     By.XPATH,
        #     '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]/span/span',
        # )
        # user1 = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[14]/div/div/div[2]/div[1]/div[1]/span/span')
        # user1 = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(user))
        # user1 = driver.find_element_by_xpath(
        #     """//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span/span[@title = "{}"]""".format(
        #         # """/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/span/span[@title = "{}"]""".format(
        #         user
        #     )
        #     # '//*[@id="pane-side"]/div/div'
        # )
        user1.click()
        print(user1.get_attribute("title"))
        # [print(usr1.get_attribute("title")) for usr1 in user1]
        # for u in user:
        #     print(str(u.text))
        # user.click()
        #  copyable-text selectable-text
        # <div class="_3u328 copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div>
        msg_box = driver.find_element_by_xpath(
            """//*[@id="main"]/footer/div[1]/div[2]/div"""
        ).click()
        msg_box = driver.find_element_by_xpath(
            """//*[@id="main"]/footer/div[1]/div[2]/div/div[@class="copyable-text" and @class="selectable-text"]"""
        )
        msg_box.send_keys(msg)
        driver.find_element_by_class_name("compose-btn-send").click()
    # time.sleep(50000)
    driver.quit()
except Exception as e:
    print(e)
    driver.quit()
