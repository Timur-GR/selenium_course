from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element(By.TAG_NAME, "form").click()


finally:
	time.sleep(20)
	browser.quit()