from selenium.webdriver.common.by import By
from selenium import webdriver
import data

driver = webdriver.Chrome()
driver.get(data.around_link)
email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')

assert email.get_attribute('placeholder') == 'Correo electrónico'
assert password.get_attribute('placeholder') == 'Correo electrónico'

driver.quit()
