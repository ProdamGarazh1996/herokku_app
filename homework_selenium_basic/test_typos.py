import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.basic
@pytest.mark.smoke
def test_add_remove_elements(browser):
    correct_text = "Sometimes you'll see a typo, other times you won't."
    browser.get("https://the-internet.herokuapp.com/typos")
    WebDriverWait(browser, 30).until(
        lambda d: d.execute_script(
            "return document.readyState") == "complete")
    elements = browser.find_elements(By.TAG_NAME, "p")
    error_text = 'Опечатка в тексте: ' + elements[1].text
    assert correct_text == elements[1].text, error_text
    browser.refresh()
