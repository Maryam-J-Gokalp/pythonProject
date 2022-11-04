import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from os.path import join, dirname

chrome_options = Options()

chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

chrome_driver = os.getcwd() + "/chromedriver"
print(chrome_driver)

def BCC_test():
    browser = webdriver.Chrome();

   # service \= Service(executable_path=ChromeDriverManager().install())
   # browser = webdriver.Chrome(service=service, options=chrome_options)
    print('Testing Process Started: ')

    # userIsOnTheHomePage()
    browser.get("https://www.bbc.co.uk/news")
    print('Website Opened')

    time.sleep(10)

    # userClicksSignInButtonAtTheTopOfTheScreen
    signInBtn = browser.find_element("xpath", '//*[@id="idcta-link"]')
    signInBtn.click()
    time.sleep(10)

    # userEntersUsername 
    emailInput = browser.find_element("xpath", '//*[@type="email"]')
    emailInput.send_keys("test@testing.com")
    time.sleep(10)

    # userEntersPassword
    smallPasswordInput = browser.find_element("xpath", '//*[@type="password"]')
    smallPasswordInput.send_keys("tiny")
    time.sleep(10)

    signInBtn = browser.find_element("xpath" ,'//*[@type="submit"]')
    signInBtn.click()
    time.sleep(10)
    # sorryThatPasswordIsTooShortItNeedsToBeEightCharactersOrMore
    # passwordTooShortMsg = browser.find_element("xpath", '//*[@aria-live="assertive"]')
    # if passwordTooShortMsg != None:
    # True


    browser.quit()


BCC_test()