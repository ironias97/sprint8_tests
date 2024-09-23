from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import data

driver = webdriver.Chrome()
driver.get(data.around_link)

# Iniciar sesión
WebDriverWait(driver, 2).until((EC.visibility_of_element_located((By.ID, 'email')))).send_keys('josue@hotmail.com')
WebDriverWait(driver, 2).until((EC.visibility_of_element_located((By.ID, 'password')))).send_keys('Josue123')

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'auth-form__button'))).click()

# Hacer clic en la foto de perfil
WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "profile__image"))).click()

# # Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = data.avatar_url
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# # Guardar la nueva foto
driver.find_element(By.XPATH,
                    "//div[@class='popup popup_type_edit-avatar popup_is-opened']//button[@type='submit' and text()='Guardar']").click()

# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"), 'style', avatar_url))

style = driver.find_element(By.CLASS_NAME, 'profile__image').get_attribute("style")
# Comprobar que style contiene el enlace a la foto de perfil
print(style)
print(avatar_url)
assert avatar_url in style
driver.quit()
