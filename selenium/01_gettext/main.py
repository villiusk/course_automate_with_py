from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:/opt/chromewebdriver/107/chromedriver.exe')

def get_driver():
  options =webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximazed")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControled")

  driver= webdriver.Chrome(service=service, options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  return text.split(": ")[1]

def main():
  driver = get_driver()
  time.sleep(2)
  element=driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())