from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")


# try:
#     WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))
#     driver.find_element(By.ID, 'email').send_keys('juan.perez@hotmail.com')
#     driver.find_element(By.ID, 'password').send_keys('password123')
#     WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, ".//button[@class='auth-form__button']"))
#     ).click()
# except Exception as e:
#     print(f"No se pudo encontrar el botón: {e}")
# time.sleep(3)

driver.find_element(By.ID, 'email').send_keys('juan.perez@hotmail.com')

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, 'password').send_keys('password123')

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()


# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))


# Comprobar que la URL actual es 'https://around-v1.nm.tripleten-services.com/signin?lng=es'
assert driver.current_url == 'https://around-v1.nm.tripleten-services.com/signin?lng=es'

driver.quit()