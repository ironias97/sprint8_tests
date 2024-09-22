from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')

assert email.get_attribute('placeholder') == 'Correo electrónico'
assert password.get_attribute('placeholder') == 'Correo electrónico'

driver.quit()
