import allure
import requests

import data
from helper import mail_generator, password_generator, name_generator, payload_new_user
from data import post_register_user, del_user_data, exist_user_email


@allure.description('Класс тестирования пользователя. Создание и удаление.')
class TestCreateUser:

    @allure.title('Создаём и потом удаляем пользователя. Есть accessToken - значит создался.')
    def test_create_user_true(self):
        response = requests.post(post_register_user, data=payload_new_user())
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200

        del_user = requests.delete(del_user_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == data.user_delete_202 and del_user.status_code == 202

    @allure.title('Нельзя создать 2х одинаковых пользователей. Передали существующий email. Ожидаем ошибку 403.')
    def test_cant_create_two_same_user_false(self):
        payload = {
        "email": exist_user_email,
        "password": password_generator(),
        "name": name_generator()
            }
        response = requests.post(post_register_user, data=payload)
        assert response.json() == data.user_error_403_exists and response.status_code == 403

    @allure.title('Создаем пользователя без поля Email. Ожидаем ошибку 403.')
    def test_missing_email_data_false(self):
        payload = {
        "email": "",
        "password": password_generator(),
        "name": name_generator()
        }
        response = requests.post(post_register_user, data=payload)
        assert response.json() == data.user_error_403_no_required_fields and response.status_code == 403

    @allure.title('Создаем без обязательного поля Password. Ожидаем ошибку 403.')
    def test_missing_password_data_false(self):
        payload = {
            "email": mail_generator(),
            "password": "",
            "name": name_generator()
        }
        response = requests.post(post_register_user, data=payload)
        assert response.json() == data.user_error_403_no_required_fields and response.status_code == 403

    @allure.title('Создаем пользователя без name. Ожидаем ошибку 403.')
    def test_missing_name_data_true(self):
        payload = {
            "email": mail_generator(),
            "password": password_generator(),
            "name": ""
        }
        response = requests.post(post_register_user, data=payload)
        assert response.json() == data.user_error_403_no_required_fields and response.status_code == 403

    @allure.title('Создаем пользователя без всех полей. Ожидаем ошибку 403.')
    def test_cant_create_without_fields_false(self):
        payload = {
            "email": "",
            "password": "",
            "name": ""
        }
        response = requests.post(post_register_user, data=payload)
        assert response.json() == data.user_error_403_no_required_fields and response.status_code == 403
