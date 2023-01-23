from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from datetime import datetime
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

def save_value(val):
    now=datetime.now()
    filename=now.strftime("%Y-%m-%d_%H%M%S.txt")
    with open(filename,'w') as f:
        f.write(str(val))

def main():
  driver = get_driver("http://automated.pythonanywhere.com")
  while True:
      time.sleep(2)
      element=driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
      value=clean_text(element.text)
      print(value)
      save_value(value)

  
main()

