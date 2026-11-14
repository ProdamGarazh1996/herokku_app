from pathlib import Path

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.advanced
@pytest.mark.smoke
def test_file_upload(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("https://the-internet.herokuapp.com/upload")
    browser.maximize_window()
    file_path = Path("images.jpg").resolve()
    browser.find_element(By.ID, "file-upload").send_keys(str(file_path))
    browser.find_element(By.ID, "file-submit").click()
    uploaded = wait.until(EC.visibility_of_element_located(
        (By.ID, "uploaded-files")))
    assert uploaded.text == file_path.name
