import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.regression
@pytest.mark.parametrize('action, expected',
                         [(Keys.ARROW_UP, "1"),
                          (Keys.ARROW_DOWN, "-1")])
def test_inputs(browser, action, expected):
    error_text = 'Значение инпут значения не соответсвует ожидаемому'
    browser.get("https://the-internet.herokuapp.com/inputs")
    browser.maximize_window()
    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys(action)
    assert input_field.get_attribute("value") == expected, error_text
