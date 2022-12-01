import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

WEBSITE = "https://docs.google.com/forms/d/e/1FAIpQLSfRml1m6uhyk4YqCmbXqYnifNu-Hmdgy4EYWkAzOSHy7l5w9w/viewform"
DRIVER_PATH = os.getcwd() + "//drivers//chromedriver.exe"
WAIT_TIME = 5
WAIT_TIME_EACH_ITEM = 0.2

s = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=s)
driver.get(WEBSITE)
time.sleep(WAIT_TIME)

INPUT_EMAIL = "dsvignacio@gmail.com"
INPUT_NAME = "Ignacio, Dennis Salvador Valeza"
INPUT_LUGAR_NA_PINANGGALINGAN = "Area 2"
INPUT_SAAN_NAGPUNTA_NAKARAANG_2_ARAW = "Area 2"
INPUT_ILAN_CLOSE_CONTACT = "2"

########################################################
#       Email
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
FIND_ELEMENT.send_keys(INPUT_EMAIL)
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Full name (Last, Given)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
FIND_ELEMENT.send_keys(INPUT_NAME)
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Rason ng pagpunta sa Kalay (Dormer)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="i13"]')
FIND_ELEMENT.click()
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Lugar na pinanggalingan (address)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
FIND_ELEMENT.send_keys(INPUT_LUGAR_NA_PINANGGALINGAN)
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Status ng Bakuna konta COVID-19 (meron lahat)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div')
FIND_ELEMENT.click()
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Sintomas (wala lahat)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[18]/span/div[3]/div/div')
FIND_ELEMENT.click()
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[20]/span/div[3]/div/div')
FIND_ELEMENT.click()
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Paraan sa pagpunta sa Kalay (Naglakad)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="i44"]')
FIND_ELEMENT.click()
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Saan nagpunta nitong nakaraang dalawang araw?
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')
FIND_ELEMENT.send_keys(INPUT_SAAN_NAGPUNTA_NAKARAANG_2_ARAW)
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       Ilan ang inyong naging close contact?
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')
FIND_ELEMENT.send_keys(INPUT_ILAN_CLOSE_CONTACT)
time.sleep(WAIT_TIME_EACH_ITEM)


########################################################
#       May alam ka bang kaso ng Covid-19 sa iyong mga napuntahan? (Wala)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="i89"]')
FIND_ELEMENT.click()
time.sleep(WAIT_TIME_EACH_ITEM)

########################################################
#       May alam ka bang kaso ng Covid-19 malapit sa inyong lugar? (Wala)
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="i99"]')
FIND_ELEMENT.click()
time.sleep(WAIT_TIME_EACH_ITEM)

########################################################
#       CLICK BUTTON
########################################################
FIND_ELEMENT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div')
FIND_ELEMENT.click()
time.sleep(WAIT_TIME)

driver.close()
driver.quit()
