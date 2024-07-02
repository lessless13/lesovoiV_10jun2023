import allure
import time
from python_tests.locators import Urls
from selenium.webdriver.common.by import By
from random import randint
from python_tests.locators import Modals, Carusel, Cart
from python_tests.conftest import PERMISSIBLE_TIME_TO_WAIT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import random




@allure.title("Тест проверяет корзину.")
@allure.step('Заходим на главную, добавляем случайный товар в корзину, убеждаемся, что успешно добавили, '
             'изменяем количество, далее удаляем из корзины')
def test_check_cart(web_driver):

    web_driver.get(Urls.MAIN_PAGE)

    WebDriverWait(web_driver, PERMISSIBLE_TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.XPATH, Modals.CHOOSE_CITY_BY_XPATH))
    )
    web_driver.find_element(By.XPATH, Modals.CHOOSE_CITY_BY_XPATH).click()

    WebDriverWait(web_driver, PERMISSIBLE_TIME_TO_WAIT).\
        until(EC.element_to_be_clickable((By.XPATH, Modals.NO_SUBSCRIPTION_BY_XPATH)))
    web_driver.find_element(By.XPATH, Modals.NO_SUBSCRIPTION_BY_XPATH).click()


    web_driver.execute_script("window.scrollTo(0, 900)")


    slider_items_title = web_driver.find_element(By.CLASS_NAME, Carusel.ITEM_IN_SLIDER_BY_CLASS)\
        .find_elements(By.XPATH, Carusel.ITEMM_TITLE_BY_XPATH)

    buy_buttons = web_driver.find_element(By.CLASS_NAME, Carusel.ITEM_IN_SLIDER_BY_CLASS)\
        .find_elements(By.XPATH, Carusel.BUY_BUTTON_BY_XPATH)

    random_book = randint(0, 5)
    print(random_book)
    assertion_title = slider_items_title[random_book].text
    print(assertion_title)
    time.sleep(1)
    buy_buttons[random_book].click()

    WebDriverWait(web_driver, PERMISSIBLE_TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.XPATH, Cart.MINI_CART_BADGE_BY_XPATH)))

    web_driver.get(Urls.MAIN_PAGE + Urls.CART)

    WebDriverWait(web_driver, PERMISSIBLE_TIME_TO_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, Carusel.ITEMM_TITLE_BY_XPATH))
    )

    book_title = web_driver.find_element(By.XPATH, Carusel.ITEMM_TITLE_BY_XPATH).text
    print(book_title)

    assert assertion_title == book_title


    WebDriverWait(web_driver, PERMISSIBLE_TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.CLASS_NAME, Cart.PRODUCT_QUANTITY_BY_CLASS)))
    product_quantity = web_driver.find_element(By.CLASS_NAME, Cart.PRODUCT_QUANTITY_BY_CLASS)
    print('Первично книг в корзине ' + str(product_quantity.text))

    product_add = web_driver.find_element(By.XPATH, Cart.ADD_ITEM)
    product_add.click()
    time.sleep(4)
    web_driver.refresh()
    time.sleep(3)
    WebDriverWait(web_driver, PERMISSIBLE_TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.CLASS_NAME, Cart.PRODUCT_QUANTITY_BY_CLASS)))

    product_quantity = web_driver.find_element(By.CLASS_NAME, Cart.PRODUCT_QUANTITY_BY_CLASS)
    print('Книг в корзине ' + str(product_quantity.text))
    assert str('2') in product_quantity.text

    time.sleep(1)
    web_driver.find_element(By.CLASS_NAME, Cart.DELETE_BOOK_BY_CLASS).click()
    time.sleep(1)
    book_removed = web_driver.find_element(By.CLASS_NAME, Cart.BOOK_REMOVED_BY_CLASS)
    print(book_removed.text)
    assert book_removed.text == 'Удалили товар из корзины.'




