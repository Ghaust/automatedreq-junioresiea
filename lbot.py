#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time


def log_into_linkedin(driver):
    username = driver.find_element_by_id('username')
    username.send_keys("junior-esiea@et.esiea.fr")
    password = driver.find_element_by_id('password')
    password.send_keys(unicode("passwordstillfakebecauseofsecurity", 'utf-8')) 
    password.send_keys(Keys.RETURN)
    print('connection successful')


def searchSomeone(driver, name):
    search = driver.find_element_by_class_name('search-global-typeahead__input')
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    print('search step')
    
def addAlumni(driver):
    try:
        sendInvit_button = driver.find_element_by_xpath('//button[@class="search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary"]')
        sendInvit_button.click()
        time.sleep(2)

        print("invitation sent")
        
        addNote_button = driver.find_element_by_xpath('//button[@aria-label="Ajouter une note"]')
        addNote_button.click()
        message = "Junior ESIEA bot used to create the Alumni group. You will be able to reconnect with your old friends, network and keep track on our JE. We sent you a request because you were a member of Junior ESIEA or PIER at ESIEA. If you have never belonged to these  associations, please ignore this message."

        textarea = driver.find_element_by_xpath('//textarea[@id="custom-message"]')
        textarea.send_keys(message)
        
        sendText_button = driver.find_element_by_xpath('//button[@class="ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')
        sendText_button.click()
        print("message sent")
        
    except:
        print("request already sent or alumni already in your network")
   
def readAlumns(filename, driver):
    alumn_number = 0
    alumnis = open(filename, 'r')
    for alumni in alumnis:
        alumn_number+=1
        searchSomeone(driver, unicode(alumni,'utf-8'))
        time.sleep(5)
        addAlumni(driver)
        driver.get('https://www.linkedin.com/mynetwork/')
    print("we have successfully added "+ alumn_number + " to the group !")
    
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