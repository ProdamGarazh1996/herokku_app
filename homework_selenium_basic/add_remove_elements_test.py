from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    driver.maximize_window()
    button_add = driver.find_element(
        By.XPATH, "//button[text()='Add Element']")
    button_add.click()
    button_add.click()
    button_delete = driver.find_element(By.XPATH, "//button[text()='Delete']")
    button_delete.click()
    delete_elements = driver.find_elements(
        By.XPATH, "//button[text()='Delete']")
    error = ('Ожидаемое количество элементов: 1'
             ' DELETE не соответствует фактическому: ') + str(
        len(delete_elements))
    assert len(delete_elements) == 1, error
finally:
    driver.quit()
