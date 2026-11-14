import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.advanced
@pytest.mark.smoke
def test_dynamic_controls(browser):
    wait = WebDriverWait(browser, 30)
    browser.get("https://the-internet.herokuapp.com/dynamic_controls")
    browser.maximize_window()
    browser.find_element(By.XPATH, "//button[text()='Remove']").click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//p[text()=\"It's gone!\"]")))
    wait.until(EC.invisibility_of_element_located((By.ID, "checkbox")))
    input_element = browser.find_element(By.XPATH, "//input[@type='text']")
    assert not input_element.is_enabled(), "Поле ввода активно"
    browser.find_element(By.XPATH, "//button[text()='Enable']").click()
    wait.until(EC.visibility_of_element_located((
        By.XPATH, "//p[text()=\"It's enabled!\"]")))
    assert input_element.is_enabled(), "Поле ввода неактивно"
