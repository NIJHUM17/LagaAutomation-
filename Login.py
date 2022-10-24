import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("D:/Python/chromedriver.exe")
driver = webdriver.Chrome(service=s)

#Login
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
print(driver.title)
time.sleep(2)
driver.find_element("xpath", "//a[@class='login']").click()
time.sleep(2)

driver.find_element("id", "email").send_keys("tahsinanijum5199@gmail.com")
time.sleep(2)

driver.find_element("id", "passwd").send_keys("123Nipu")
time.sleep(1)
driver.find_element("xpath", "//button[@id='SubmitLogin']").click()

#Search

driver.find_element("id", "search_query_top").send_keys("dress")
driver.find_element("xpath", "//button[@name='submit_search']").click()
time.sleep(2)