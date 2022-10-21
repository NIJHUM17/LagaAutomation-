import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

email = "tahsinanijum5199@gmail.com"
firstname = "Tahsin Adiba"
lastname = "Nijhum"
password = "123Nipu"
address = "Downey"
addressLine2 = "Dominant Dream"
city = "South Gate"
state = "California"
zip_code = "90280"
Home_phone = "+12022563030"
mobile = "+8801629099448"

driver = webdriver.Chrome(executable_path="D:/Python/chromedriver.exe")

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
print(driver.title)
time.sleep(1)
driver.find_element("xpath", "//a[@class='login']").click()
time.sleep(1)

driver.find_element("id", "email_create").send_keys(email)
time.sleep(2)
driver.find_element("xpath", "//button[@id='SubmitCreate']").click()
time.sleep(1)

# Registration

#driver.find_element("xpath", "//div[@class=radio]")
driver.find_element("id", "id_gender2").click()

driver.find_element("id", "customer_firstname").send_keys(firstname)
time.sleep(1)
driver.find_element("id", "customer_lastname").send_keys(lastname)
time.sleep(1)
driver.find_element("id", "passwd").send_keys(password)
time.sleep(1)
driver.find_element("id", "days").send_keys(17)
time.sleep(1)
driver.find_element("id", "months").send_keys("February")
time.sleep(1)
driver.find_element("id", "years").send_keys(2000)
time.sleep(1)

driver.find_element("xpath", "//input[@id='newsletter']").click()
driver.find_element("xpath", "//input[@id='optin']").click()

#######


driver.find_element("id", "firstname").send_keys(firstname)

driver.find_element("id", "lastname").send_keys(lastname)

driver.find_element("id", "company").send_keys(company)

driver.find_element("id", "address1").send_keys(address)

driver.find_element("id", "address2").send_keys(addressLine2)

driver.find_element("id", "city").send_keys(city)

driver.find_element("id", "id_state").send_keys(state)

driver.find_element("id", "postcode").send_keys(zip_code)

driver.find_element("id", "other").send_keys("Information will be added later if needed")

driver.find_element("id", "phone").send_keys(Home_phone)

driver.find_element("id", "phone_mobile").send_keys(mobile)

driver.find_element("id", "alias").send_keys(address)

driver.find_element("xpath", "//button[@id='submitAccount']").click()
