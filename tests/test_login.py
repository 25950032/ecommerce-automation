
import pytest
import allure

from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Successful login")
@allure.title("Login successfully with valid credentials")
@allure.description("""
Verify that a user can log in successfully
using valid credentials and access the products page.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_exitoso(page):

    with allure.step("1. Open SauceDemo"):
        login = LoginPage(page)
        login.abrir()

    with allure.step("2. Enter valid credentials"):
        login.iniciar_sesion(
            "standard_user",
            "secret_sauce"
        )

    with allure.step("3. Verify products page"):
        assert page.locator(".title").inner_text() == "Products"


@pytest.mark.parametrize(
    "usuario, password, mensaje_esperado",
    [
        (
            "standard_user",
            "password123",
            "Username and password do not match"
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Sorry, this user has been locked out"
        ),
    ]
)
@allure.feature("Login")
@allure.story("Invalid login")
@allure.title("Reject invalid login credentials: {usuario}")
@allure.description("""
Verify that the application displays the appropriate
error message when login credentials are invalid
or the user account is locked.
""")
@allure.severity(allure.severity_level.NORMAL)
def test_login_con_datos_invalidos(
    page,
    usuario,
    password,
    mensaje_esperado
):

    with allure.step("1. Open SauceDemo"):
        login = LoginPage(page)
        login.abrir()

    with allure.step(f"2. Attempt login with user: {usuario}"):
        login.iniciar_sesion(usuario, password)

    with allure.step("3. Verify login error message"):
        mensaje = login.mensaje_error.inner_text()
        assert mensaje_esperado in mensaje
