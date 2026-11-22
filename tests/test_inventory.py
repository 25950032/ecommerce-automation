
import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def iniciar_aplicacion(page):

    login = LoginPage(page)

    login.abrir()

    login.iniciar_sesion(
        "standard_user",
        "secret_sauce"
    )

    return InventoryPage(page)


@allure.feature("Inventory")
@allure.story("Product catalog")
@allure.title("TC04 - Verify product catalog")
@allure.description("""
Verify that the inventory page displays the correct title
and all six available products.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_visualizar_catalogo(page):

    with allure.step("1. Log in to SauceDemo"):
        inventario = iniciar_aplicacion(page)

    with allure.step("2. Verify inventory page title"):
        assert inventario.obtener_titulo() == "Products"

    with allure.step("3. Verify number of products"):
        assert inventario.contar_productos() == 6


@allure.feature("Inventory")
@allure.story("Product information")
@allure.title("TC05 - Verify product names and prices")
@allure.description("""
Verify that the product catalog displays six names
and six prices, including Sauce Labs Backpack at $29.99.
""")
@allure.severity(allure.severity_level.NORMAL)
def test_datos_productos(page):

    with allure.step("1. Log in and open product catalog"):
        inventario = iniciar_aplicacion(page)

    with allure.step("2. Retrieve product names and prices"):
        nombres = inventario.obtener_nombres()
        precios = inventario.obtener_precios()

    print("Nombres:", nombres)
    print("Precios:", precios)

    print(
        "Elementos inventory_item_name:",
        page.locator(".inventory_item_name").count()
    )

    print(
        "Elementos inventory_item:",
        page.locator(".inventory_item").count()
    )

    with allure.step("3. Verify product information"):
        assert len(nombres) == 6
        assert len(precios) == 6
        assert "Sauce Labs Backpack" in nombres
        assert "$29.99" in precios


@allure.feature("Inventory")
@allure.story("Shopping cart")
@allure.title("TC06 - Add product to shopping cart")
@allure.description("""
Verify that a user can add Sauce Labs Backpack
to the shopping cart and that the cart badge displays 1.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_agregar_producto_carrito(page):

    with allure.step("1. Log in and open product catalog"):
        inventario = iniciar_aplicacion(page)

    with allure.step("2. Add backpack to shopping cart"):
        inventario.agregar_mochila()

    with allure.step("3. Verify shopping cart counter"):
        assert inventario.obtener_contador_carrito() == "1"


@allure.feature("Inventory")
@allure.story("Shopping cart")
@allure.title("TC07 - Remove product from shopping cart")
@allure.description("""
Verify that a user can remove Sauce Labs Backpack
from the shopping cart and that the cart badge disappears.
""")
@allure.severity(allure.severity_level.NORMAL)
def test_eliminar_producto_carrito(page):

    with allure.step("1. Log in and open product catalog"):
        inventario = iniciar_aplicacion(page)

    with allure.step("2. Add backpack to shopping cart"):
        inventario.agregar_mochila()

    with allure.step("3. Remove backpack from shopping cart"):
        inventario.eliminar_mochila()

    with allure.step("4. Verify shopping cart is empty"):
        assert inventario.contador_carrito.count() == 0
