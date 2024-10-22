# тут ручки собрал.
main_url = 'https://stellarburgers.nomoreparties.site'
post_user = f'{main_url}/api/auth/register'
del_user = f'{main_url}/api/v1/user/:'
login_user = f'{main_url}/api/auth/login'
create_order= f'{main_url}/api/v1/orders'



# заготовки ожидаемых текстов ответов
user_error_403_exists = {"success": False, "message": "User already exists"}
user_error_403__no_required_fields =  {"success": False, "message": "Email, password and name are required fields"}
# user_create_ok_200 = {"success": "true"}
user_2same_create_error_409 = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
user_no_login_pass_create_error_400 = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
user_2same_logins_create_error_409 = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}