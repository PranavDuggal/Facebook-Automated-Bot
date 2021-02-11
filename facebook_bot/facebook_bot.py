import requests
import random
import json
import selenium
import time
import re
import io
import sys
import pyautogui
import pydirectinput
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from numpy import random
from friends import friends

with open('config.json') as file:
        config = json.load(file)

username = config['username']
password = config['password']


options=webdriver.ChromeOptions()
options.headless=False

prefs={"profile.default_content_setting_values.notifications", 2}
driver = webdriver.Chrome(executable_path="C:/Users/prana/OneDrive/Documents/chromedriver.exe",chrome_options=options)
driver.maximize_window()
driver.get('https://www.facebook.com/')
time.sleep(5)

email_text = driver.find_element_by_id('email')
email_text.send_keys(username)
password_txt = driver.find_element_by_id('pass')
password_txt.send_keys(password)

driver.find_element_by_id('u_0_d').click()
time.sleep(3)
print("Redirecting to profile page")   
driver.get("https://www.facebook.com/profile.php")
time.sleep(5)


# friend_name="John"
# search_bar = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/label/input")
# search_bar.click()
# search_bar.send_keys(friend_name)
# pydirectinput.moveTo(100, 150) 
# pydirectinput.press('enter')
# time.sleep(3)
# pydirectinput.moveTo(1568,390)
# time.sleep(3)
# driver.get("https://www.facebook.com")
# time.sleep(3)
#post = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
#post.click()
#time.sleep(3)
#post_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div')
#post_text.send_keys('I am a Bot')
#time.sleep(3)
#post_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]')
#post_button.click()
#time.sleep(3)
# driver.get("https://www.facebook.com/profile.php")

x = random.choice(range(1,9))
friend = friends[x]
# friend_comment = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[9]/div[1]/a")
friend_comment = driver.find_element_by_xpath(friend)
friend_comment.click()
time.sleep(5)
