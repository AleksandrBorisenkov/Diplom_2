import allure
import requests

import data
from data import patch_change_user_data, del_user_data, post_register_user, exist_user_email
from helper import mail_generator, name_generator, payload_new_user, password_generator


@allure.description('Класс изменение данных пользователя')
class TestChangeUserData:

    @allure.title('Пробуем изменить данные пользователя. Токен не верный. Ожидаем ошибку 403')
    def test_broken_token_user_change_data(self):
        auth_token = "Bearer eyJhbGciOiJIU"
        patch_email = {"email": mail_generator()}
        change_profile_data = requests.patch(patch_change_user_data, headers={"authorization": auth_token}, data=patch_email)
        assert change_profile_data.json() == data.user_error_403_token_bad_change_data and change_profile_data.status_code == 403

    @allure.title('Пробуем изменить данные не авторизованным пользователем. Токен не передан. Ожидаем ошибку 401')
    def test_unauthorized_user_change_data(self):
        patch_email = {"email": mail_generator()}
        change_profile_data = requests.patch(patch_change_user_data, headers={"authorization": ""}, data=patch_email)
        assert change_profile_data.json() == data.user_error_401_unauthorized_change_data and change_profile_data.status_code == 401

    @allure.title('Создаем, логинемся, изменяем имя пользователя. Потом удаляем пользователя. Ожидаем успех 200 и 202')
    def test_chage_profile_name_true(self):
        patch_name = {"name": name_generator()}
        new_user = requests.post(post_register_user, data=payload_new_user())
        auth_token = new_user.json()["accessToken"]
        change_profile_data = requests.patch(patch_change_user_data, headers={"authorization": f"{auth_token}"}, data=patch_name)
        assert change_profile_data.json()["success"] == True and change_profile_data.status_code == 200

        del_user = requests.delete(del_user_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == data.user_delete_202 and del_user.status_code == 202

    @allure.title('Создаем, логинемся, изменяем email пользователя. Потом удаляем пользователя. Ожидаем успех 200 и 202')
    def test_chage_profile_email_true(self):
        patch_email = {"email": mail_generator()}
        new_user = requests.post(post_register_user, data=payload_new_user())
        auth_token = new_user.json()["accessToken"]
        change_profile_data = requests.patch(patch_change_user_data, headers={"authorization": f"{auth_token}"}, data=patch_email)
        assert change_profile_data.json()["success"] == True and change_profile_data.status_code == 200

        del_user = requests.delete(del_user_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == data.user_delete_202 and del_user.status_code == 202

    @allure.title('Создаем, логинемся, изменяем email пользователя. Потом удаляем пользователя. Ожидаем успех 200 и 202')
    def test_chage_profile_password_true(self):
        patch_password = {"email": password_generator()}
        new_user = requests.post(post_register_user, data=payload_new_user())
        auth_token = new_user.json()["accessToken"]
        change_profile_data = requests.patch(patch_change_user_data, headers={"authorization": f"{auth_token}"}, data=patch_password)
        assert change_profile_data.json()["success"] == True and change_profile_data.status_code == 200

        del_user = requests.delete(del_user_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == data.user_delete_202 and del_user.status_code == 202

    @allure.title('Создаем, логинемся, изменяем email пользователя на существующий в систему. Потом удаляем пользователя. Ожидаем ошибку 403 и успех 202')
    def test_chage_profile_mail_false(self):
        patch_email = {"email": exist_user_email}
        new_user = requests.post(post_register_user, data=payload_new_user())
        auth_token = new_user.json()["accessToken"]
        change_profile_data = requests.patch(patch_change_user_data, headers={"authorization": f"{auth_token}"}, data=patch_email)
        assert change_profile_data.json()["success"] == False and change_profile_data.status_code == 403

        del_user = requests.delete(del_user_data, headers={"authorization": f"{auth_token}"})
        assert del_user.json() == data.user_delete_202 and del_user.status_code == 202
