from selenium.webdriver.common.by import By
from selenium import webdriver
import data

driver = webdriver.Chrome()
driver.get(data.around_link)
driver.find_element(By.CSS_SELECTOR,'.auth-form__title')

driver.quit()