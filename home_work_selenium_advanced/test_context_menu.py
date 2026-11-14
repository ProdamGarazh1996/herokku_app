import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.advanced
@pytest.mark.regression
def test_context_menu(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("https://the-internet.herokuapp.com/context_menu")
    browser.maximize_window()
    action_chains = ActionChains(browser)
    (action_chains.move_to_element(browser.find_element(By.ID, "hot-spot"))
     .context_click().perform())
    alert = wait.until(EC.alert_is_present())
    assert alert.text == 'You selected a context menu', \
        "Текст на алерте не соответствует ожидаемому"
