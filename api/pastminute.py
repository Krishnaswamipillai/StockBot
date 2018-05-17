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

browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

def fetchMinute(ticker):
    url = "http://www.morningstar.com"
    browser.get(url)
    time.sleep(5)

    elem = browser.find_element_by_css_selector("span.icon.remove-ui-icon")
    print(elem)

    elem.click()

    time.sleep(2)

    inputElement = browser.find_element_by_css_selector("input.qa-automation-search")
    inputElement.click()

    inputElement.send_keys(ticker)

    inputElement.send_keys(Keys.ENTER)
    time.sleep(1)
    browser.find_element_by_class_name('chart-iframe-full-chart-label').click();
    time.sleep(1)
    browser.find_element_by_class_name('mkts-cmpt-svgcht-menuText').click();
