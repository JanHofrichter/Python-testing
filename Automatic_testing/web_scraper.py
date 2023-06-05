import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "Automatic testing/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")

time.sleep(1)

authorization = driver.find_element(By.ID, "L2AGLb")
authorization.click()

time.sleep(1)

search = driver.find_element(By.ID, "APjFqb")
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)

time.sleep(1)

div_element = driver.find_element(By.CLASS_NAME, "kno-rdesc")
span_text = div_element.find_element(By.TAG_NAME, "span")
text = span_text.text
print(text)

driver.quit

