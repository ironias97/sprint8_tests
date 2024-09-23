from selenium import webdriver
import time
import data

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(data.around_link)
assert '/signin' in driver.current_url
time.sleep(5)
driver.quit()