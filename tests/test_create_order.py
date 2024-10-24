import json
from random import random

import allure
import requests
import random

import data
from data import get_ingredients, post_login_user, exist_user_payload, post_create_order
from helper import password_generator


def return_random_ingredient():
    get_info = requests.get(get_ingredients)
    data_text = json.loads(get_info.text)
    ingredients = [element['_id'] for element in data_text['data']]
    return random.choice(ingredients)

@allure.description('Класс создания заказа для не авторизованных пользователей.')
class TestUnauthorizedCreateOrder:

    @allure.title('Создаем заказ если не авторизован и есть ингредиент. Ожидаем успех 200')
    def test_unauthorized_create_order_with_ingredients_true(self):
        ingredients = {"ingredients": [return_random_ingredient()]}
        create_order = requests.post(post_create_order, ingredients)
        assert create_order.json()["success"] == True and create_order.status_code == 200
        print(create_order.json(), create_order.status_code)

    @allure.title('Создаем заказ если не авторизован и нет ингридиента. Ожидаем ошибку 400')
    def test_unauthorized_create_order_without_ingredients_false(self):
        ingredients = {"ingredients": []}
        create_order = requests.post(post_create_order, ingredients)
        assert create_order.json() == data.no_ingredient_error_400 and create_order.status_code == 400
        print(create_order.json(), create_order.status_code)

    @allure.title('Создаем заказ если не авторизован и невалидный HASH ингридиента. Ожидаем ошибку 500')
    def test_unauthorized_create_order_with_badhash_ingredients_false(self):
        ingredients = {"ingredients": [password_generator()]}
        create_order = requests.post(post_create_order, ingredients)
        assert create_order.status_code == 500



@allure.description('Класс создания заказа для авторизованных пользователей - значит передан токен при заказе.')
class TestLoginUserCreateOrder:

    @allure.title('Создаем заказ если юзер авторизован, передан токен, и есть ингредиент. Ожидаем успех 200')
    def test_login_user_create_order_with_ingredients_true(self):
        ingredients = {"ingredients": [return_random_ingredient()]}
        response = requests.post(post_login_user, data=exist_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200

        create_order = requests.post(post_create_order, headers={"authorization": f"{auth_token}"}, data=ingredients)
        assert create_order.json()["success"] == True and create_order.status_code == 200

    @allure.title('Создаем заказ если юзер авторизован, передан токен, и нет ингридиента. Ожидаем ошибку 400')
    def test_login_user_create_order_without_ingredients_false(self):
        ingredients = {"ingredients": []}
        response = requests.post(post_login_user, data=exist_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200

        create_order = requests.post(post_create_order, headers={"authorization": f"{auth_token}"}, data=ingredients)
        assert create_order.json() == data.no_ingredient_error_400 and create_order.status_code == 400

    @allure.title('Создаем заказ если юзер авторизован, передан токен, и невалидный HASH ингридиента. Ожидаем ошибку 500')
    def test_login_user_create_order_with_badhash_ingredients_false(self):
        ingredients = {"ingredients": [password_generator()]}
        response = requests.post(post_login_user, data=exist_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200

        create_order = requests.post(post_create_order, headers={"authorization": f"{auth_token}"}, data=ingredients)
        assert create_order.status_code == 500
