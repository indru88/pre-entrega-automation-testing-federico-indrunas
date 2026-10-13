"""Funciones auxiliares para los tests de SauceDemo."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL_BASE = "https://www.saucedemo.com"
USUARIO = "standard_user"
PASSWORD = "secret_sauce"
TIMEOUT = 10


def crear_driver():
    """Abre Chrome maximizado. Selenium 4 se encarga de bajar el driver."""
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")
    opciones.add_experimental_option(
        "prefs",
        {"credentials_enable_service": False, "profile.password_manager_enabled": False},
    )
    return webdriver.Chrome(options=opciones)


def esperar_visible(driver, localizador, timeout=TIMEOUT):
    """Espera explícita hasta que el elemento sea visible y lo devuelve."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(localizador)
    )


def hacer_login(driver, usuario=USUARIO, password=PASSWORD):
    """Completa el formulario de login y espera a que cargue el inventario."""
    driver.get(URL_BASE)
    esperar_visible(driver, (By.ID, "user-name")).send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/inventory.html"))
