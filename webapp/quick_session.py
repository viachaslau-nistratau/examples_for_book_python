from flask import Flask, session

# создаем новое приложение Flask
app = Flask(__name__)
# инициализируем генератор Flask секретным ключом
app.secret_key = 'YouWillNeverGuess'

@app.route('/session/<user>')
def setuser(user: str) -> str:
    # значение переменной user присваивается ключу user в словаре session
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return "User value is currently set to: " + session['user']

if __name__ == '__main__':
    app.run(debug=True)
