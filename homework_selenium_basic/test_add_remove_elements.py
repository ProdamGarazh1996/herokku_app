import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.smoke
def test_add_remove_elements(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    browser.maximize_window()
    button_add = browser.find_element(
        By.XPATH, "//button[text()='Add Element']")
    button_add.click()
    button_add.click()
    button_delete = browser.find_element(By.XPATH, "//button[text()='Delete']")
    button_delete.click()
    delete_elements = browser.find_elements(
        By.XPATH, "//button[text()='Delete']")
    error = ('Ожидаемое количество элементов: 1'
             ' DELETE не соответствует фактическому: ') + str(
        len(delete_elements))
    assert len(delete_elements) == 1, error
