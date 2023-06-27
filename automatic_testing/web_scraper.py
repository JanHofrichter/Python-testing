import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

log_format = "%(asctime)s %(levelname)s %(name)s: %(message)s" 
logging.basicConfig(level = logging.INFO, format = log_format)

def main():
    #Setting driver
    PATH = "Automatic testing/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    logging.info("Selenium is starting")
    
    #Check if code runs without problems
    try:
        driver.maximize_window()
        driver.get("https://google.com")
        logging.info("opening https://google.com")

        time.sleep(2)

        cookies = driver.find_element(By.XPATH, "//div[contains(@class,'QS5gu sy4vM')]")
        cookies.click()
        logging.info("Accepting cookies is done")

        time.sleep(2)

        search = driver.find_element(By.XPATH, "//textarea[contains(@class,'gLFyf')]")
        search.send_keys("Selenium")
        search.send_keys(Keys.ENTER)

        time.sleep(2)

        div_element = driver.find_element(By.CLASS_NAME, "kno-rdesc")
        span_text = div_element.find_element(By.TAG_NAME, "span")
        text = span_text.text
        logging.info("Get info about Selenium: {}".format(text))
    
    except Exception as e:
        logging.exception("An error occured: {}".format(e))
  
    
    driver.quit
    logging.info("Selenium closed")


if __name__ == '__main__':
    main()

