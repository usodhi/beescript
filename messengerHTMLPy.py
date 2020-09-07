from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import sys

# this is something that has to be downloaded
driver = webdriver.Chrome(
    r'C:\\Users\\udayv\\OneDrive\\Documents\\Brown\\CSCI\\Fun\\chromedriver')

driver.get("https://www.facebook.com/messages/t/100010621808295")

wait = WebDriverWait(driver, 600)

# this is the person / group you want to send it to
target = '"massive"'

# this is the file with the script
beeMovie = open("colt45.txt")

text = beeMovie.read()

beeMovie.close()

# x_arg = '//span[contains(@title,' + target + ')]'

# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))

# print(group_title)
# print("Wait for few seconds")
# group_title.click()
message = driver.find_elements_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]//div[1]/div/div/div/div/div/div[1]/div/div/div')[0]

wordToSend = ''
for word in text:
    if word == ' ':
        message.send_keys(wordToSend)
        sendbutton = driver.find_elements_by_xpath(
            '//*[@id="content"]/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a')[0]
        sendbutton.click()
        wordToSend = ''

    else:
        wordToSend += word
        if word == text[len(text) - 1]:
            message.send_keys(wordToSend)
            sendbutton = driver.find_elements_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click()


driver.close()
