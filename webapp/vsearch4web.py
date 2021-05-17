
from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """
    функция записи (добавления) в конец файла vsearch.log (значение 'a')
    """
    with open('vsearch.log', 'a') as log:
        # print(req.form, file=log, end='|')         # данные из HTML-формы веб-приложения
        # print(req.remote_addr, file=log, end='|')  # IP-адрес веб-браузера, приславшего форму
        # print(req.user_agent, file=log, end='|')   # строка, идентифицирующая браузер пользовател
        # print(res, file=log)
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search():  # -> html:
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
    return render_template('entry.html',
                           the_tittle='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log():  # -> html:
    """
    функция обработки запроса с URL /viewlog
    """
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', "Remote_addr", 'User_agent', 'Results')
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
