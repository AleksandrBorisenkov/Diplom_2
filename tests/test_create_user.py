import allure
import pytest
import requests

import data
from helper import mail_generator, password_generator, name_generator
from data import post_user

@allure.description('Класс тестирования пользователя. Создание.')
class TestCreateCourier:

    @allure.title('Создание пользователя с разными данным и сопоставление с результатом из документации, сверяя что есть accessToken.')
    def test_create_user_true(self):
        payload = {
        "email": mail_generator(),
        "password": password_generator(),
        "name": name_generator()
        }
        response = requests.post(post_user, data=payload)
        assert "accessToken" in response.json() and response.status_code == 200

    @allure.title('Нельзя создать 2х одинаковых пользователей. Данные существующего в системе пользователя. Ожидаем ошибку 403')
    def test_cant_create_two_same_user_false(self):
        payload = {
        "email": "51253@yandex.ru",
        "password": "12613612",
        "name": "151361"
            }
        response = requests.post(post_user, data=payload)
        assert response.json() == data.user_error_403_exists and response.status_code == 403

    @allure.title('Создаем без обязательного поля Login. Ожидаем ошибку 403.')
    def test_missing_email_data_false(self):
        payload = {
        "email": "",
        "password": password_generator(),
        "name": name_generator()
        }
        response = requests.post(post_user, data=payload)
        assert response.json() == data.user_error_403__no_required_fields and response.status_code == 403

    @allure.title('Создаем без обязательного поля Password. Ожидаем ошибку 403.')
    def test_missing_password_data_false(self):
        payload = {
            "email": mail_generator(),
            "password": "",
            "name": name_generator()
        }
        response = requests.post(post_user, data=payload)
        assert response.json() == data.user_error_403__no_required_fields and response.status_code == 403

    @allure.title('Создаем без name. Ожидаем успех 403.')
    def test_missing_fname_data_true(self):
        payload = {
            "email": mail_generator(),
            "password": password_generator(),
            "name": ""
        }
        response = requests.post(post_user, data=payload)
        assert response.json() == data.user_error_403__no_required_fields and response.status_code == 403

    @allure.title('Создаем без всех полей. Ожидаем ошибку 403.')
    def test_cant_create_two_same_emails_true(self):
        payload = {
            "email": "",
            "password": "",
            "name": ""
        }
        response = requests.post(post_user, data=payload)
        assert response.json() == data.user_error_403__no_required_fields and response.status_code == 403
