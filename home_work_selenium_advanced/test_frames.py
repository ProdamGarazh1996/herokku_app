import pytest
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.regression
def test_frames(browser):
    browser.get("https://the-internet.herokuapp.com/iframe")
    browser.maximize_window()
    iframe = browser.find_element(By.ID, "mce_0_ifr")
    browser.switch_to.frame(iframe)
    text_element = browser.find_element(By.XPATH, "//body[@id='tinymce']//p")
    assert text_element.text == "Your content goes here."
    browser.switch_to.default_content()
