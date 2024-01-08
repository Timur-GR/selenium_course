from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
	return str(int(x)+int(y))

link = 'https://suninjuly.github.io/selects1.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
	x = x_element.text
	y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
	y = y_element.text
	z = calc(x, y)

	select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
	select.select_by_value(z)

	browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()



finally:
	time.sleep(20)
	browser.quit()