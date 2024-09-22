from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
WebDriverWait(driver, 5).until((EC.visibility_of_element_located((By.ID, 'email')))).send_keys('josue@hotmail.com')
WebDriverWait(driver, 5).until((EC.visibility_of_element_located((By.ID, 'password')))).send_keys('Josue123')

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'auth-form__button'))).click()

# Hacer clic en la foto de perfil

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "profile__image"))).click()

# # Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "owner-avatar"))).send_keys(avatar_url)
#
# # Guardar la nueva foto
# driver.find_element(By.CLASS_NAME, 'popup__button').click()
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='popup popup_type_edit-avatar popup_is-opened']//button[@type='submit' and text()='Guardar']"))
    ).click()

except Exception as e:
    print("Error:", e)

# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
style = driver.find_element(By.CLASS_NAME, 'profile__image').get_attribute("style")
# Comprobar que style contiene el enlace a la foto de perfil
assert avatar_url in style
driver.quit()
