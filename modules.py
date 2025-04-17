# -*- coding: utf-8 -*-

import random

def get_random_word():
    """ Функция загружает список слов из указанного файла и выбирает случайное слово.
    :return: случайное слово из списка """
    with open("content/words.txt", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return random.choice(words)


def throw_snowball():
    """ Функция возвращает сообщение о результате броска снежка.
    :return: строка с результатом """
    messages = [
        "и попал прямо в лоб @${random.chatter} hah",
        "и снёс шапку @${random.chatter} jebaited",
        "и попал в плечо @${random.chatter} aa",
        "и попал в ногу @${random.chatter} Upal",
        "и промахнулся. Как же @${random.chatter} повезло wawa",
        "и оказалось, что это была граната. buhFlipExplode Тебя взорвали, @${random.chatter}",
        "и забросил @${random.chatter} прямо за шиворот. Strashno Как холодно",
        "и попал прямо по попе @${random.chatter} spank ОЙ!",
        "и разбил окно дома @${random.chatter} oh",
        "и удивил всех размером своего снежного кома. Словно в боулинге, ком сбивает несколько целей с ног "
                + "@${random.chatter} " * random.randint(2, 4) + "SHTO",
        "и оказалось, что это был @${random.chatter}. Он закинул его прямо в руки @${random.chatter} SHTO"
    ]
    return random.choice(messages)


def get_cat_fact():
    with open("content/cats.txt", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return random.choice(words)