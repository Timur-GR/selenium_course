from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_syndyk = browser.find_element(By.CSS_SELECTOR, "#treasure")
	x = x_syndyk.get_attribute("valuex")
	y = calc(x)

	browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
	browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
	browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
	browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
	time.sleep(10)
	browser.quit()
