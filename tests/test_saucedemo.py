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


def test_catalogo(driver):
    hacer_login(driver, USUARIO, PASSWORD)

    assert driver.title == "Swag Labs"

    esperar_visible(driver, (By.CLASS_NAME, "inventory_item"))
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en el inventario"

    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()

    primero = productos[0]
    nombre = primero.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primero.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {nombre} - {precio}")
    assert nombre != ""
    assert precio.startswith("$")