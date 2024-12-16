from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("./chromedriver.exe")  # Sürücü yolunu buraya doğru şekilde belirtin
driver = webdriver.Chrome(service=service)

url="https://www.youtube.com/"
driver.get(url)

time.sleep(3)
print(driver.title)
driver.maximize_window()
driver.save_screenshot('homepage.png')

url="https://github.com/kbunall"
driver.get(url)

time.sleep(3)

driver.back()
time.sleep(3)
driver.close()

