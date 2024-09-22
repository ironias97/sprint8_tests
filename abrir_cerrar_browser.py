from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
assert '/signin' in driver.current_url
time.sleep(5)
driver.quit()