# -*- coding: utf-8 -*-

from flask import Flask
from modules import get_random_word, throw_snowball, get_cat_fact, ball8

# Создаём приложение Flask
app = Flask(__name__)

# Определяем маршрут для получения случайного слова
@app.route('/random_word', methods=['GET'])
def random_word():
    word = get_random_word()
    return word

# Определяем маршрут для "кинуть снежок"
@app.route('/snejok', methods=['GET'])
def snejok():
    message = throw_snowball()
    return message

@app.route('/cat_fact', methods=['GET'])
def cat_fact():
    fact = get_cat_fact()
    return fact

@app.route('/8ball', methods=['GET'])
def ball8():
    message = ball8
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)