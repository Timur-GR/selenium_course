from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
  

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)

	browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
	browser.find_element(By.CSS_SELECTOR, "[for=robotCheckbox]").click()
	browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
	browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
	time.sleep(20)
	browser.quit()

