from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
	for element in elements:
		element.send_keys("Мой ответ")

	
	current_dir = os.path.abspath(os.path.dirname('lesson2.2_step8.py'))   
	file_path = os.path.join(current_dir, 'test.txt')
	element.send_keys(file_path)


finally:
	time.sleep(20)
	browser.quit()