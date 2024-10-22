import random

# сгенерирровали почту
def mail_generator():
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    name = ''.join(random.choice(letters) for i in range(10))
    domain = ''.join(random.choice(letters) for i in range(6))
    country = ['ru', 'com', 'org', 'by', 'mail', 'rus', 'net', 'uk', 'us']
    mail = name + '@' + domain + '.' + random.choice(country)
    return mail

# сгенерировали пароль
def password_generator():
    ls = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    password = ''.join(random.choice(ls) for i in range(0, 10))
    return password

# сгенерировали имя и фамилию
def name_generator():
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    frs_name = ''.join(random.choice(letters) for i in range(10))
    lst_name = ''.join(random.choice(letters) for i in range(10))
    return f"{frs_name} {lst_name}"
