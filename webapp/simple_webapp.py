from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is a page 1'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is a page 2'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is a page 3'


# код для обработки URL '/login'
@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    # используем метод pop ждя удаления ключа logged_in session
    session.pop('logged_in')
    return'You are now logged out'


# установление значения для секретного ключа приложения
app.secret_key = 'YouWillNeverGuessMySecretKey'

# @app.route('/status')
# def check_status() -> str:
#     # ключ 'logged_in' существует в словаре session?
#     if 'logged_in' in session:
#         # если да, вернуть это сообщение
#         return 'You are currently logged in.'
#     # если нет, вернуьб это сообщение
#     return 'You are NOT logged in.'


if __name__ == '__main__':
    app.run(debug=True)
