import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.

def test_user_should_see_add_to_basket_button(browser):
    print("\nОткрываем страницу товара..")
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    
    try:
        print("\nОжидаем пока кнопка не станет доступной..")
        button_add = WebDriverWait(browser, 5).until(
            EC.element_to_be_clicable((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )

        assert button_add.is_displayed(), "Кнопка не видна/не отображается"
    
    except NoSuchElementExeption:
        assert False, "Кнопка не найдена"
