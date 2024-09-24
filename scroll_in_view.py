from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data

driver = webdriver.Chrome()
driver.get(data.around_link)
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "email")))
# Iniciar sesión
driver.find_element(By.ID, "email").send_keys(data.email)
driver.find_element(By.ID, "password").send_keys(data.password)
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))


# Buscar la tarjeta y desplazarla a la vista
element = driver.find_element(By.CSS_SELECTOR, ".places__item")
driver.execute_script("arguments[0].scrollIntoView();", element)


driver.quit()