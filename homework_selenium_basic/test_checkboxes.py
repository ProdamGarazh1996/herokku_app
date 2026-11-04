import pytest
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.regression
def test_add_remove_elements(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    browser.maximize_window()
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    if not checkboxes[0].is_selected():
        checkboxes[0].click()
    assert checkboxes[0].is_selected(), 'Первый чекбокс не был отмечен'
    if checkboxes[1].is_selected():
        checkboxes[1].click()
    assert not checkboxes[1].is_selected(), 'Второй чекбокс остался отмеченым'
