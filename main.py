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

# # Importing package to output random strings
from essential_generators import DocumentGenerator
gen = DocumentGenerator()

# Import X Paths of friend grid on profile page
from friends import friends

# Import the class
from facebook_bot.fb_bot import Facebook_Bot

# Import user details stored as json
with open('config.json') as file:
        config = json.load(file)

# Setting up chrome driver
options=webdriver.ChromeOptions()
options.headless=False
prefs={"profile.default_content_setting_values.notifications", 2}
driver = webdriver.Chrome(executable_path="Driver\chromedriver.exe",chrome_options=options)

##############################################################################################
# Facebook Bot Flow
# 1. Login
# 2. Open account profile page
# 3. Add a friend
# 4. Write a post from home page
# 5. Open a random friends profile and write a post

bot = Facebook_Bot(driver,config,friends)


bot.login() # Logs into the facebook account


bot.open_profile() # Opens the Profile Page


bot.add_friend() # This Function helps to add a Friend


bot.write_post(gen.sentence()) # This Helps in posting a message on your profile


# bot.open_friends_profile_randomly() # This functions Randomly chooses a friend in your friends list
bot.post_on_friends_profile(gen.sentence()) # This opens a friends profile randomly and writes a post


