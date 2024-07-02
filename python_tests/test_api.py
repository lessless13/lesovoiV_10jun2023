import allure
from selenium.webdriver.common.by import By
import time
from python_tests import Urls




@allure.title("Тест проверяет корзину. Часть 1")
@allure.step('Заходим на главную, добавляем случайный товар в корзину, убеждаемся, что успешно добавили')
def test_check_bed_tags(web_driver):
    web_driver.get()
