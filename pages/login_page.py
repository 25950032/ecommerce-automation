
class LoginPage:

    def __init__(self, page):
        self.page = page

        self.campo_usuario = page.locator("#user-name")
        self.campo_password = page.locator("#password")
        self.boton_login = page.locator("#login-button")
        self.mensaje_error = page.locator("[data-test='error']")

    def abrir(self):
        self.page.goto("https://www.saucedemo.com/")

    def iniciar_sesion(self, usuario, password):
        self.campo_usuario.fill(usuario)
        self.campo_password.fill(password)
        self.boton_login.click()
