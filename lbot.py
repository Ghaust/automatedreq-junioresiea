#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import pyautogui as pag
import time

#def goto_signinpage(driver):
#    try:
#        driver.find_element_by_class("sign-in-card__dismiss-btn").click()
#    except:
#        print(driver)
        
def log_into_linkedin(driver):
    username = driver.find_element_by_id('username')
    username.send_keys("junior-esiea@et.esiea.fr")
    password = driver.find_element_by_id('password')
    password.send_keys(unicode("passwordstillfakebecauseofsecurity", 'utf-8')) #
    password.send_keys(Keys.RETURN)
    print('connection successful')


def searchSomeone(driver, name):
    search = driver.find_element_by_class_name('search-global-typeahead__input')
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    search.send_keys("tamere")
    print('search step')
    
def addAlumni(driver):
    try:
        sendInvit_button = driver.find_element_by_xpath('//button[@class="search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary"]')
        sendInvit_button.click()
        time.sleep(2)

        print("invitation sent")
        
        addNote_button = driver.find_element_by_xpath('//button[@aria-label="Ajouter une note"]')
        addNote_button.click()
        message = "Junior ESIEA bot used to create the Alumni group. We sent you a friend request because you were a member of Junior ESIEA or PIER, the small entreprise of the engineering school ESIEA."

        textarea = driver.find_element_by_xpath('//textarea[@id="custom-message"]')
        textarea.send_keys(message)
        
        sendText_button = driver.find_element_by_xpath('//button[@class="ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')
        sendText_button.click()
        print("message sent")
        #print(sendText_button.get_attribute('outerHTML'))
    except:
        print("request already sent or alumni already in your network")
   
def readAlumns(filename, driver):
    alumnis = open(filename, 'r')
    for alumni in alumnis:
        searchSomeone(driver, unicode(alumni,'utf-8'))
        time.sleep(5)
        addAlumni(driver)
        driver.get('https://www.linkedin.com/mynetwork/')
    
def main():
    url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    driver = webdriver.Firefox()
    driver.get(url)
    #goto_signinpage(browser)
    log_into_linkedin(driver)
    time.sleep(5)
    readAlumns("alumnis.txt", driver)
    
    
    
    
if __name__ == "__main__":
    main()