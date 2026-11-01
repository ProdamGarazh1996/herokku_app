from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    error_text = 'Значение инпут значения не соответсвует ожидаемому'
    driver.get("https://the-internet.herokuapp.com/inputs")
    driver.maximize_window()
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys(Keys.ARROW_UP)
    assert input_field.get_attribute("value") == "1", error_text
    input_field.send_keys(Keys.ARROW_DOWN)
    assert input_field.get_attribute("value") == "0", error_text
finally:
    driver.quit()
