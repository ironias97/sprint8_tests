from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
driver = webdriver.Chrome()
driver.get(data.around_link)
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
# Iniciar sesión
driver.find_element(By.ID, "email").send_keys(data.email)
driver.find_element(By.ID, "password").send_keys(data.password)
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Hacer clic en la foto de perfil
driver.find_element(By.CSS_SELECTOR, ".profile__image").click()

# Insertar un enlace a la nueva foto
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# Guardar la nueva foto
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Guardar']").click()

# Esperando a que se cargue la foto de perfil
WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"), 'style', avatar_url))

style = driver.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute('style')
assert avatar_url in style
driver.quit()