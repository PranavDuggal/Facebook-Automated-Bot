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

from facebook_bot.fb_bot import Facebook_Bot

with open('config.json') as file:
        config = json.load(file)

# Import class from facebook.py file


options=webdriver.ChromeOptions()
options.headless=False
prefs={"profile.default_content_setting_values.notifications", 2}
driver = webdriver.Chrome(executable_path="C:/Users/prana/OneDrive/Documents/chromedriver.exe",chrome_options=options)


bot = Facebook_Bot(driver,config,friends)


bot.login()
bot.open_profile()

from essential_generators import DocumentGenerator
gen = DocumentGenerator()
bot.write_post(gen.sentence())


bot.open_friends_profile_randomly()



