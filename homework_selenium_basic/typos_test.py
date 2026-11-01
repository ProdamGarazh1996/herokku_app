from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
try:
    reload_count = 10
    correct_text = "Sometimes you'll see a typo, other times you won't."
    driver.get("https://the-internet.herokuapp.com/typos")
    for i in range(1, reload_count + 1):
        print(f'Попытка №{i}')
        WebDriverWait(driver, 30).until(
            lambda d: d.execute_script(
                "return document.readyState") == "complete")
        elements = driver.find_elements(By.TAG_NAME, "p")
        error_text = 'Опечатка в тексте: ' + elements[1].text
        assert correct_text == elements[1].text, error_text
        driver.refresh()
finally:
    driver.quit()
