from selenium.webdriver.common.by import By

from utils.helpers import (
    PASSWORD,
    USUARIO,
    esperar_visible,
    hacer_login,
)


def test_login_exitoso(driver):
    hacer_login(driver, USUARIO, PASSWORD)

    assert "/inventory.html" in driver.current_url
    titulo_seccion = esperar_visible(driver, (By.CLASS_NAME, "title"))
    assert titulo_seccion.text == "Products"
    assert driver.title == "Swag Labs"