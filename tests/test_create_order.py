import json
from random import random

import allure
import requests
import random

import data
from data import get_ingredients


def return_random_ingredient():
    get_info = requests.get(get_ingredients)
    data_text = json.loads(get_info.text)
    ingredients = [element['_id'] for element in data_text['data']]
    return random.choice(ingredients)

@allure.description('Класс создания заказа для не авторизованных пользователей')
class TestUnauthorizedCreateOrder:

    @allure.title('Создаем заказ если не авторизован и есть ингредиент. Ожидаем успех 200')
    def test_unauthorized_create_order_with_ingredients_true(self):
        ingredients = {"ingredients": [return_random_ingredient()]}
        create_order = requests.post(data.post_create_order, ingredients)
        assert create_order.json()["success"] == True and create_order.status_code == 200
        print(create_order.json(), create_order.status_code)

    @allure.title('Создаем заказ если не авторизован и нет ингридиента. Ожидаем ошибку 400')
    def test_unauthorized_create_order_without_ingredients_false(self):
        ingredients = {"ingredients": []}
        create_order = requests.post(data.post_create_order, ingredients)
        assert create_order.json() == data.no_ingredient_error_400 and create_order.status_code == 400
        print(create_order.json(), create_order.status_code)

    @allure.title('Создаем заказ если не авторизован и невалидный HASH ингридиента')
    def test_unauthorized_create_order_with_badhash_ingredients_false(self):
        ingredients = {"ingredients": ["61c1f82001bdaaa6f"]}
        create_order = requests.post(data.post_create_order, ingredients)
        assert create_order.status_code == 500

@allure.description('Класс создания заказа для авторизованных пользователей')
class TestLoginUserCreateOrder:

    @allure.title('Создаем заказ если не авторизован и есть ингредиент. Ожидаем успех 200')
    def test_unauthorized_create_order_with_ingredients_true(self):
        ingredients = {"ingredients": [return_random_ingredient()]}
        create_order = requests.post(data.post_create_order, ingredients)
        assert create_order.json()["success"] == True and create_order.status_code == 200
        print(create_order.json(), create_order.status_code)

    @allure.title('Создаем заказ если не авторизован и нет ингридиента. Ожидаем ошибку 400')
    def test_unauthorized_create_order_without_ingredients_false(self):
        ingredients = {"ingredients": []}
        create_order = requests.post(data.post_create_order, ingredients)
        assert create_order.json() == data.no_ingredient_error_400 and create_order.status_code == 400
        print(create_order.json(), create_order.status_code)

    @allure.title('Создаем заказ если не авторизован и невалидный HASH ингридиента')
    def test_unauthorized_create_order_with_badhash_ingredients_false(self):
        ingredients = {"ingredients": ["61c1f82001bdaaa6f"]}
        create_order = requests.post(data.post_create_order, ingredients)
        assert create_order.status_code == 500
