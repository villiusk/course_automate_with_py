from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service('C:/opt/chromewebdriver/107/chromedriver.exe')

def get_driver(url):
  options =webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximazed")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControled")

  driver= webdriver.Chrome(service=service, options=options)
  driver.get(url)
  return driver

def clean_text(text):
  return float(text.split(": ")[1])

def main():
  driver = get_driver("http://automated.pythonanywhere.com/login")
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  #print(driver.current_url)
  time.sleep(3)
  element=driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())