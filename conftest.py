from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def download_dir():
    path = Path(__file__).parent / "downloads"
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture
def browser(download_dir):
    chrome_options = Options()
    prefs = {
        "download.default_directory": str(download_dir.resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
