from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
imgs =driver.find_elements(By.XPATH,'.//img')
assert len(imgs) >1

driver.quit()