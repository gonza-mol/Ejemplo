import pytest
from pytest_bdd import scenarios, given, when, then, scenario, parsers
from selenium import webdriver
from pytest_bdd import given
from selenium import webdriver



PAGINA_WEB = 'https://automationteststore.com/'


scenarios('../features/ejemplo.feature')
def test_ejemplo():
    pass

@pytest.fixture
def browser():
    b = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\PruebaError\\Drivers\\chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()


@given('Pagina web')
def irPaginaDeLogin(browser):
    browser.get(PAGINA_WEB)

@when('ingreso "usuario" y contraseña "password"')
def ingresar_Usuario_Pass():
    #browser.find_element_by_css_selector('customer_menu_top').click()
   # browser.implicity_wait(100)
   print("Estoy en el segundo paso")


@then('login válido')
def verificar_titulo():
    #assert browser.find_element_by_css_selector('h1 span.maintext').text == 'MY ACCOUNT'
    print("Estoy en el tercer paso")

