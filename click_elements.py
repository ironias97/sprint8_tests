from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data

driver = webdriver.Chrome()
driver.get(data.around_link)

# driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[@class='auth-form__button']"))
    ).click()
except Exception as e:
    print(f"No se pudo encontrar el botón: {e}")


driver.quit()
