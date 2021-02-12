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
driver = webdriver.Chrome(executable_path="Enter the executable path for chromedriver here",chrome_options=options)
driver.maximize_window()
driver.get('https://www.facebook.com/')
time.sleep(5)

email_text = driver.find_element_by_id('email')         # Entering Email
email_text.send_keys(username)
password_txt = driver.find_element_by_id('pass')        # Entering Password
password_txt.send_keys(password)

driver.find_element_by_id('u_0_d').click()              # Clicking The Login Button
time.sleep(3)
print("Redirecting to profile page")   
driver.get("https://www.facebook.com/profile.php")
time.sleep(5)


friend_name="Enter any of your Friend's Name Here"      
search_bar = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/label/input")  # Enters the Name into search bar and searches
search_bar.click()
search_bar.send_keys(friend_name)
pydirectinput.moveTo(100, 150)     # Moves the Cursor to the Search Bar and Send the signal to keyboard to press enter 
pydirectinput.press('enter')
time.sleep(3)
pydirectinput.moveTo(1568,390)     # Moves the cursor towards the Add Friend button and signals the cursor to click the button
pydirectinput.click()
time.sleep(3)
# This Part is used to post a message on the post box in Facebook
driver.get("https://www.facebook.com")
time.sleep(3)
post = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
post.click()
time.sleep(3)
post_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div')
post_text.send_keys('I am a Bot')
time.sleep(3)
post_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]')
post_button.click()
time.sleep(3)
driver.get("https://www.facebook.com/profile.php")

# This Part randomly chooses a Friend from your Friends List
x = random.choice(range(1,9))
friend = friends[x]
friend_comment = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[9]/div[1]/a")
# friend_comment = driver.find_element_by_xpath(friend)
friend_comment.click()
time.sleep(5)
