from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service("./chromedriver.exe")  # Sürücü yolunu buraya doğru şekilde belirtin
driver = webdriver.Chrome(service=service)

url="https://github.com"
driver.get(url)
driver.maximize_window()
searchinput=driver.find_element_xpath("//*[@id="query-builder-test"]")
time.sleep(1)

searchinput.send_keys("python")
time.sleep(2)
searchinput.send_keys(Keys.ENTER)
time.sleep(4)
driver.close()
# //*[@id="query-builder-test"]