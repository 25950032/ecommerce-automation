
import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Checkout")
@allure.story("Complete purchase")
@allure.title("Complete purchase successfully")
@allure.description("""
Verify that a registered user can complete an entire purchase.

Test flow:
1. Log in to the application.
2. Add a product to the cart.
3. Verify the cart contents.
4. Complete the checkout information.
5. Verify the order summary.
6. Finish the purchase and verify confirmation.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_compra_completa(page):

    # 1. Iniciar sesión
    with allure.step("1. Log in to SauceDemo"):
        login = LoginPage(page)
        login.abrir()
        login.iniciar_sesion(
            "standard_user",
            "secret_sauce"
        )

    # 2. Agregar producto
    with allure.step("2. Add backpack to the cart"):
        inventario = InventoryPage(page)
        inventario.agregar_mochila()

    # 3. Abrir carrito
    with allure.step("3. Open shopping cart"):
        carrito = CartPage(page)
        carrito.abrir_carrito()

    # Diagnóstico del carrito
    with allure.step("4. Verify cart contents"):
        print("\n===== DIAGNOSTICO DEL CARRITO =====")
        print("URL:", page.url)

        print(
            "Contador del carrito:",
            page.locator(
                "[data-test='shopping-cart-badge']"
            ).all_inner_texts()
        )

        print(
            "Productos cart_item:",
            page.locator(".cart_item").count()
        )

        print(
            "Productos inventory_item:",
            page.locator(".inventory_item").count()
        )

        print("===================================")

        assert carrito.contar_productos() == 1

    # 5. Iniciar checkout
    with allure.step("5. Start checkout"):
        carrito.iniciar_checkout()

    # 6. Completar datos
    with allure.step("6. Enter customer information"):
        checkout = CheckoutPage(page)

        checkout.completar_datos(
            "Andrea",
            "Kohn",
            "3700"
        )

    # 7. Continuar
    with allure.step("7. Continue to order summary"):
        checkout.continuar()
        page.wait_for_url("**/checkout-step-two.html")

    # Diagnóstico del resumen
    with allure.step("8. Verify order summary"):
        print("\n===== RESUMEN DE COMPRA =====")
        print("URL:", page.url)

        print(
            "Productos cart_item:",
            page.locator(".cart_item").count()
        )

        print(
            "Productos inventory_item:",
            page.locator(".inventory_item").count()
        )

        print(
            "Nombres encontrados:",
            page.locator(
                ".inventory_item_name"
            ).all_inner_texts()
        )

        print("=============================")

        assert page.locator(".cart_item").count() == 1

    # 9. Finalizar compra
    with allure.step("9. Finish purchase"):
        checkout.finalizar_compra()

    # 10. Verificar confirmación
    with allure.step("10. Verify purchase confirmation"):
        assert checkout.obtener_confirmacion() == (
            "Thank you for your order!"
        )
