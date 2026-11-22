
class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.nombre = page.locator("#first-name")
        self.apellido = page.locator("#last-name")
        self.codigo_postal = page.locator("#postal-code")

        self.boton_continue = page.locator(
            "[data-test='continue']"
        )

        self.boton_finish = page.locator(
            "[data-test='finish']"
        )

        self.confirmacion = page.locator(
            ".complete-header"
        )

    def completar_datos(
        self, nombre, apellido, codigo_postal
    ):

        self.nombre.fill(nombre)
        self.apellido.fill(apellido)
        self.codigo_postal.fill(codigo_postal)

    def continuar(self):
        self.boton_continue.click()

    def finalizar_compra(self):
        self.boton_finish.click()

    def obtener_confirmacion(self):
        return self.confirmacion.inner_text()
