import pytest
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def file_is_downloaded(directory: Path):
    files = [
        f for f in directory.iterdir()
        if f.is_file() and not f.name.startswith(".") and not f.name.endswith(
            (".crdownload", ".tmp"))
    ]
    return files[0] if files else False


@pytest.mark.advanced
@pytest.mark.regression
def test_file_download(browser, download_dir):
    browser.get("https://the-internet.herokuapp.com/download")

    file_link = browser.find_element(By.XPATH, "//a[text()='Images.txt']")
    expected_filename = file_link.text
    file_link.click()

    # Используем стандартный WebDriverWait
    downloaded_file = WebDriverWait(browser, 15).until(
        lambda d: file_is_downloaded(download_dir),
        message="Файл не успел скачаться за 15 секунд"
    )

    assert downloaded_file.exists(), "Файл не найден в файловой системе"
    assert downloaded_file.name == expected_filename
    assert downloaded_file.stat().st_size > 0
