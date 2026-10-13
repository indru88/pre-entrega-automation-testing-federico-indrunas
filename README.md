# Pre-entrega: automatización de SauceDemo

Pruebas automatizadas sobre [saucedemo.com](https://www.saucedemo.com).

## Qué se prueba

| Test | Qué valida |
|------|-----------|
| `test_login_exitoso` | Login con `standard_user`, redirección a `/inventory.html` y título "Products" / "Swag Labs" |
| `test_catalogo` | Título de la página, que haya productos, menú y filtro visibles, y nombre/precio del primero |
| `test_agregar_al_carrito` | Agrega el primer producto, el contador pasa a 1 y el ítem aparece en el carrito |

Cada test arranca su propio navegador, así que son independientes entre sí.

## Tecnologías

- Python 3
- Pytest + pytest-html
- Selenium WebDriver (Chrome)
- Git / GitHub

## Estructura

```
tests/    casos de prueba y conftest.py (fixture del driver y capturas)
utils/    funciones auxiliares (driver, login, esperas)
reports/  reporte HTML y capturas de los fallos
```

## Instalación

Hace falta tener Chrome instalado.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar las pruebas

```bash
pytest tests -v --html=reports/reporte.html --self-contained-html
```

El reporte queda en `reports/reporte.html`. Si un test falla, se guarda una
captura en `reports/`.
