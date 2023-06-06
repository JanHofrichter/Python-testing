import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

log_format = "%(asctime)s %(levelname)s %(name)s: %(message)s" 
logging.basicConfig(level = logging.INFO, format = log_format)
logger=logging.getLogger()

def main():
    #Setting driver
    PATH = "Automatic testing/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    logging.info("Selenium is starting")
    
    try:
        driver.maximize_window()
        driver.get("https://google.com")
        logging.info("opening https://google.com")

        time.sleep(2)

        cookies = driver.find_element(By.ID, "L2AGLb")
        cookies.click()
        logging.info("Accepting cookies is done")

        time.sleep(2)

        search = driver.find_element(By.ID, "APjFqb")
        search.send_keys("Selenium")
        search.send_keys(Keys.ENTER)

        time.sleep(2)

        div_element = driver.find_element(By.CLASS_NAME, "kno-rdesc")
        span_text = div_element.find_element(By.TAG_NAME, "span")
        text = span_text.text
        logging.info("Get info about Selenium: {}".format(text))
    
    except Exception as e:
        logger.exception("An error occured: {}".format(e))
  
    driver.quit

if __name__ == '__main__':
    main()

