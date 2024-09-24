import random
import data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(data.around_link)
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "email")))

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys(data.email)
driver.find_element(By.ID, "password").send_keys(data.password)
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Guardar el título de la tarjeta más reciente
title_before = driver.find_element(By.CLASS_NAME, 'card__title').text

# Hacer clic en el botón que publica una nueva tarjeta
driver.find_element(By.CLASS_NAME, 'profile__add-button').click()
# Generar el nuevo nombre del lugar e ingresarlo en el campo Nombre
new_title = 'Tokio' + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

driver.find_element(By.ID, "place-name").send_keys(new_title)

# Insertar el enlace a la imagen en el campo Enlace
driver.find_element(By.ID, "place-link").send_keys(data.picture_url)

# Guardar los datos
driver.find_element(By.XPATH, "//form[@name='new-card']/button[text()='Guardar']").click()

# Esperar a que aparezca el botón Eliminar
WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, ".//button[@class='card__delete-button card__delete-button_visible']")))

# Comprobar que la tarjeta tiene el título correcto
title_after = driver.find_element(By.XPATH, ".//li[@class='places__item card'][1]/div/h2").text

assert title_after == new_title

# Guardar la cantidad de tarjetas antes de eliminar
cards_before = len(driver.find_elements(By.XPATH, ".//li[@class='places__item card']"))
driver.find_element(By.XPATH,
                    ".//li[@class='places__item card']/button[@class='card__delete-button card__delete-button_visible']").click()

# Esperar a que el título de la tarjeta más reciente sea igual a title_before
WebDriverWait(driver, 3).until(
    EC.text_to_be_present_in_element((By.XPATH, ".//li[@class='places__item card'][1]/div/h2"), title_before))

# Comprobar que ahora hay una tarjeta menos
cards_after = len(driver.find_elements(By.XPATH, ".//li[@class='places__item card']"))

assert cards_after + 1 == cards_before

driver.quit()
