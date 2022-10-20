import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


email = "tahsinanijum5199@gmail.com"
firstname = "Tahsin Adiba"
lastname = "Nijhum"
driver = webdriver.Chrome(executable_path="D:/Python/chromedriver.exe")

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
print(driver.title)
time.sleep(2)

driver.find_element("xpath", "//a[@class='login']").click()
time.sleep(1)

driver.find_element("id", "email_create").send_keys(email)
time.sleep(2)
driver.find_element("xpath", "//button[@id='SubmitCreate']").click()
time.sleep(1)