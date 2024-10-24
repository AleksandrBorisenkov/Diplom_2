import allure
import requests

import data
from data import post_login_user, exist_user_payload, get_user_order, get_all_orders


@allure.description('Класс получения заказов.')
class TestTakeUserOrder:

    @allure.title('Получаем все заказы в системе, но максимум 50 последних. Авторизация не требуется. Ожидаем успех 200.')
    def test_get_all_orders_true(self):
        response = requests.get(get_all_orders)
        assert response.json()["success"] == True and response.status_code == 200
        assert "total" and "totalToday" in response.json()

    @allure.title('Пытаемся получить заказ без авторизации в системе. Ожидаем ошибку 401.')
    def test_unauthorized_get_order_false(self):
        response = requests.get(get_user_order)
        assert response.json() == data.user_error_401_unauthorized_user and response.status_code == 401

    @allure.title('Авторизуемся и получаем заказы пользователя. Ожидаем успех 200.')
    def test_get_orders_logined_user_true(self):
        response = requests.post(post_login_user, data=exist_user_payload)
        auth_token = response.json()["accessToken"]
        assert "accessToken" in response.json() and response.status_code == 200

        order_info = requests.get(get_user_order,  headers={"authorization": f"{auth_token}"})
        assert order_info.json()["success"] == True and order_info.status_code == 200
        assert "total" and "totalToday" in order_info.json()