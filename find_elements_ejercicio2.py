from selenium.webdriver.common.by import By
from selenium import webdriver
import data

driver = webdriver.Chrome()
driver.get(data.around_link)
imgs =driver.find_elements(By.XPATH,'.//img')
assert len(imgs) >1

driver.quit()