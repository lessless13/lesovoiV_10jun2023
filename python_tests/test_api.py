import allure
import time
import requests
import json

Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAxODYyNjgsImlhdCI6MTcyMDAxODI2OCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImE3YWNkYWNiYTFmMDdkNTFhMzFhZTE3ZmE3NWU2NjhiZDBiODdlZDY4MGRiODkzZDcxMzkwNWE0NmM2ZTg3OGMiLCJ0eXBlIjoxMH0.bQJgvZ2kulPlq1j2AvSmOiGiRyRXChUsmOe5ePLUx3s"
Coockie = "__ddg1_=sFUSSkQP7gb5aXUzBRE6; refresh-token=; _ym_uid=171954917680888488; _ym_d=1719549176; chg_visitor_id=d06b869a-2809-4bbd-a44c-86700c6d6b95; access-token=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAwMDc5MjYsImlhdCI6MTcxOTgzOTkyNiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjAyYzcwYjFmNWE2ZDZjODJjOGFkNWNmYzRmY2Q1N2E4OTAwYThmODNmN2RlZjAxMDk3MTBlZjM4ZTUzNGIwNTMiLCJ0eXBlIjoxMH0.kJIxKIipdZfxqlzEpqqek9J9oBhz592Wz9oNcvWyNgc; _ym_isad=2"
Id = 3043413



@allure.title("Тест добавляет новый товар в корзину")
@allure.step('Используя post запрос кладем книгу в корзину')
def test_add_new_item_api():
    ProductHeaders = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": Authorization,
        "Cache-Control": "no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0",
        "Content-Length": "104",
        "Content-Type": 'application/json',
        "Cookie": Coockie,
        "Dnt": "1",
        "Origin": "https://www.chitai-gorod.ru",
        "Priority": "u=1, i",
        "Referer": "https://www.chitai-gorod.ru/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'"
    }



    ProductBody = {
        "id": 3043413,
        "adData":
            {"item_list_name": "index",
             "product_shelf": "Новинки литературы"}
    }

    time.sleep(1)
    add_item_to_cart = requests.post('https://web-gate.chitai-gorod.ru/api/v1/cart/product',
                              headers=ProductHeaders, json=ProductBody, verify=False)

    assert add_item_to_cart.status_code == 200


    print('add_item_to_cart body = ' + add_item_to_cart.text)
    print(add_item_to_cart.headers)
    print(add_item_to_cart.status_code)


@allure.title("Тест добавляет новый товар в корзину")
@allure.step('Используя post запрос, кладем книгу в корзину')
def test_check_item_in_cart():

    ProductHeaders = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": Authorization,
        "Cache-Control": "no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0",
        "Cookie": Coockie,
        "Dnt": "1",
        "Origin": "https://www.chitai-gorod.ru",
        "Priority": "u=1, i",
        "Referer": "https://www.chitai-gorod.ru/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'"
    }

    time.sleep(1)
    check_item_in_cart = requests.get('https://web-gate.chitai-gorod.ru/api/v1/cart',
                                     headers=ProductHeaders, verify=False)

    response = check_item_in_cart.json()
    products = response['products'][0]['goodsId']
    print('Айди книги на главной странице - ' + str(products))
    print('Айди книги в корзине - ' + str(Id))

    print(products)

    assert str(products) == str(Id)




