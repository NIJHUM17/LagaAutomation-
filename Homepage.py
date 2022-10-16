import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

first_name = "Tahsin"
last_name = "Adiba"

driver = webdriver.Chrome(service=Service('D:\Python\pythonProject\BasicSelenium\drivers\chromedriver.exe'))
driver.get("http://automationpractice.com/index.php")
print(driver.title)
"""
driver.find_element("").click()
time.sleep(3)
driver.find_element("").click()
time.sleep(3)
element = driver.find_element("id", "input-firstname")
element.send_keys(first_name)

element = driver.find_element("id", "input-lastname")
element.send_keys(last_name)


driver.close()
driver.quit() """