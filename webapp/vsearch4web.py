
from flask import Flask, render_template, request, escape, session
from vsearch import search4letters
from checker import check_logged_in
from DBcm import UseDatabase

app = Flask(__name__)

# добавляем словарь с параметрами соединения
app.config['dbconfig'] = {'host': '127.0.0.1',
                        'user': 'viachaslau_nistratau',
                        'password': 'Val02061970!',
                        'database': 'vsearchlogDB', }

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


def log_request(req: "flask_request", res: str) -> None:
    """
    журналирует веб-запрос и возвращает результаты
    """
    # исправили код, используя диспетчер контекста 'UseDatabase',
    # которому передали настройки из app.config
    with UseDatabase(app.config['dbconfig']) as cursor:
    _SQL = """insert into log
        (phrase, letters, ip, browser_string, results) 
        values
        (%s, %s, %s, %s, %s)"""
    # выполняем запрос (из строки с описанием браузера
    # (хранящейся в req.user_agent) извлекается только его значение
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))


@app.route('/search4', methods=['POST'])
def do_search():  # -> html:
    """
    Извлекает данные из запроса;
    выполняет поиск; возвращает результаты
    """
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,
                           )


@app.route('/')
@app.route('/entry')
def entry_page():  # -> 'html':
    """
    Выводит HTML-форму
    """
    return render_template('entry.html',
                           the_tittle='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log():  # -> html:
    """
    Выводит содержимое файлаф журнала в виде HTML-таблицы.
    функция обработки запроса с URL /viewlog
    """
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results 
                  from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', "Remote_addr", 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,
                           )

# функция escape входит в состав
# фреймворка Flask и преобразует все специальные символы HTML
# в строке в экранированные последовательности.


if __name__ == '__main__':
    app.run(debug=True)
