from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
service = Service('/home/zheying/geckodriver')

driver = webdriver.Firefox(options=options, service=service)
driver.get('http://google.com')

print(driver.title)
driver.quit()