import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.basic
@pytest.mark.smoke
def test_add_remove_elements(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")
    browser.maximize_window()
    dropdown_element = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown_element)
    all_options = select.options
    assert len(all_options) > 0, "Дропдаун пуст, элементы не найдены!"
    print(f"Успешно: Найдено элементов в дропдауне — {len(all_options)}")
    for option in all_options:
        if option.is_enabled():
            print(f"Доступный вариант: {option.text}")
            select.select_by_visible_text(option.text)
            assert option.is_selected(), ('Доступный вариант "'
                                          + option.text +
                                          '" не был выбран')
