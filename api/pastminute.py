from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
option.add_argument("download.default_directory=/Users/azb/github/StockBot/api/minute/")
options.add_argument('headless')

browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

def fetchMinute(ticker):
    url = "www.morningstar.com"
    browser.get(url)
    time.sleep(1)
    try:
        browser.find_element_by_class_name("remove-ui-icon").click()
    except:
        pass

    time.sleep(.5)

    inputElement = browser.find_element_by_class_name("qa-automation-search")
    for letter in ticker:
        inputElement.send_keys(letter)

    inputElement.send_keys(Keys.ENTER)
    time.sleep(1)
    browser.find_element_by_class_name('chart-iframe-full-chart-label').click();
    time.sleep(1)
    browser.find_element_by_class_name('mkts-cmpt-svgcht-menuText').click();
