import os

import pytest

from utils.helpers import crear_driver

CARPETA_REPORTES = os.path.join(os.path.dirname(__file__), "..", "reports")


@pytest.fixture
def driver():
    driver = crear_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Si un test falla, guarda una captura en reports/."""
    resultado = (yield).get_result()
    if resultado.when == "call" and resultado.failed and "driver" in item.funcargs:
        os.makedirs(CARPETA_REPORTES, exist_ok=True)
        ruta = os.path.join(CARPETA_REPORTES, f"fallo_{item.name}.png")
        item.funcargs["driver"].save_screenshot(ruta)
