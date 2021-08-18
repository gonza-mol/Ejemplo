import time

import pytest
from pytest_bdd import given
from selenium import webdriver

#constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

#Hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture()
def browser():
    b = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\PruebaError\\Drivers\\chromedriver.exe")
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.quit()


@given("The DockdocGo home is displayed")
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


@given('Pagina web')
def irPaginaDeLogin(browser):
    browser.get(DUCKDUCKGO_HOME)