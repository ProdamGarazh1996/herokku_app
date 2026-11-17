import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.regression
def test_checkboxes(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    browser.maximize_window()
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    assert not checkboxes[0].is_selected(), "Первый чекбокс отмечен"
    checkboxes[0].click()
    assert checkboxes[0].is_selected(), 'Первый чекбокс не был отмечен'
    assert checkboxes[0].is_selected(), "Второй чекбокс не отмечен"
    checkboxes[1].click()
    assert not checkboxes[1].is_selected(), 'Второй чекбокс остался отмеченым'
