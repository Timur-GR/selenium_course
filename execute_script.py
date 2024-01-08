from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = x_element.text
	y = calc(x)

	browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
	browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

	robotRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", robotRule)
	robotRule.click()

	browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()


finally:
	time.sleep(20)
	browser.quit()


