
class CartPage:

    def __init__(self, page):
        self.page = page

        self.productos_carrito = page.locator(
            ".cart_item"
        )

        self.boton_checkout = page.locator(
            "[data-test='checkout']"
        )

    def abrir_carrito(self):
        self.page.locator(
            ".shopping_cart_link"
        ).click()

        self.page.wait_for_url("**/cart.html")

    def contar_productos(self):
        self.productos_carrito.first.wait_for(
            state="visible",
            timeout=10000
        )
        return self.productos_carrito.count()

    def iniciar_checkout(self):
        self.boton_checkout.click()
