import pytest
import time
from pytest_bdd import scenarios, given, when, then, scenario, parsers
from selenium import webdriver


from selenium.webdriver.common.keys import Keys


#DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


scenarios('../features/DuckDuckGo.feature')

#@pytest.fixture()
#def browser():
  #  b = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\PruebaError\\Drivers\\chromedriver.exe")
  #  b.implicitly_wait(10)
  #  b.maximize_window()
  #  yield b
 #   b.quit()

#@given("The DockdocGo home is displayed")
#def ddg_home(browser):
#    browser.get(DUCKDUCKGO_HOME)


@when(parsers.parse('the users searches for "{text}"'))
def Search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)



@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element_by_id('links')
    print("paso por aquí 1")
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = browser.find_element_by_name('q')
    print("paso por aquí 2")
    #assert not search_input.get_attribute('value') == phrase
    print(phrase)


