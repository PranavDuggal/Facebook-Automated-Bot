import time
import pydirectinput
from numpy import random

from selenium.common.exceptions import *

class Facebook_Bot:

        def __init__(self,driver,config,profile_friends):
                self.driver = driver

                self.username = config['username']
                self.password = config['password']

                self.search_bar_xpath = "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/label/input"
                self.profile_friends = profile_friends

        def login(self,url='https://www.facebook.com/'):
                self.driver.maximize_window()
                self.driver.get(url)
                email_text = self.driver.find_element_by_id('email')
                email_text.send_keys(self.username)
                password_txt = self.driver.find_element_by_id('pass')
                password_txt.send_keys(self.password)
                self.driver.find_element_by_id('u_0_d').click()
                time.sleep(6)


        def open_profile(self,url="https://www.facebook.com/profile.php"):
                time.sleep(6)
                print("Redirecting to profile page")   
                self.driver.get(url)
                time.sleep(6)

        def add_friend(self,friend_name="Helen Alfcgdeggbcih Vijayvergiyasen"):
                # Possible exceptions - Name doesn't exist; Already added as a friend
                
                time.sleep(6)
                search_bar = self.driver.find_element_by_xpath(self.search_bar_xpath)
                search_bar.click()
                search_bar.send_keys(friend_name)
                pydirectinput.moveTo(100, 150)
                time.sleep(1)
                pydirectinput.moveTo(120,250) 
                pydirectinput.click()
                time.sleep(6)
                friend = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/h2/span/span/div/a')
                friend.click()
                time.sleep(3)
                add_friend = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/span/div')
                add_friend.click()
                time.sleep(6)
                

        # def cancel_friend(self):
                # cancel_request = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/span/div')
                # cancel_request.click()
                # time.sleep(6)

        def write_post(self,message = "I am a Bot",url="https://www.facebook.com"):
                # Possible exceptions: If posting same as previous in short time, throws an exception
                time.sleep(6)
                self.driver.get(url)
                time.sleep(6)
                post = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
                post.click()
                time.sleep(6)
                post_text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div')
                post_text.send_keys(message)
                time.sleep(6)
                post_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]')
                post_button.click()
                time.sleep(6)

        def open_friends_profile_randomly(self,url="https://www.facebook.com/profile.php"):                
                time.sleep(6)
                self.driver.get(url)
                time.sleep(6)
                x = random.choice(range(0,8))
                friend = self.profile_friends[x]
                friend_comment = self.driver.find_element_by_xpath(friend)
                friend_comment.click()
                time.sleep(6)

        def post_on_friends_profile(self,message):
                # Possible Exceptions - No post on profile
                self.open_friends_profile_randomly()
                time.sleep(6)
                post = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span')
                post.click()
                time.sleep(6)
                post_text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
                post_text.send_keys(message)
                time.sleep(6)
                post_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]')
                post_button.click()
                time.sleep(6)
