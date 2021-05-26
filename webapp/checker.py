from flask import session
# импортируем функцию wraps (которая является декоратором) из модуля functools
from functools import wraps


def check_logged_in(func):
    # декорируем функцию wrapper с помощью декоратора wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        # если пользователь браузера выполнил вход
        if 'logged_in' in session:
            # вызвать декорируемую функцию
            return func(*args, **kwargs)
        # иначе, вернуьб соответсвующее сообщение
        return 'You are NOT logged in.'
    return wrapper
