from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    driver.maximize_window()
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    if not checkboxes[0].is_selected():
        checkboxes[0].click()
    assert checkboxes[0].is_selected(), 'Первый чекбокс не был отмечен'
    if checkboxes[1].is_selected():
        checkboxes[1].click()
    assert not checkboxes[1].is_selected(), 'Второй чекбокс остался отмеченым'
finally:
    driver.quit()
