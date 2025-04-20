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
        "и оказалось, что это был @${random.chatter}. Он закинул его прямо в руки @${random.chatter} SHTO",
        "и тот растаял в полете. На улице слишком жарко, поэтому всего несколько капель воды попало на @${random.chatter} hot"
    ]
    return random.choice(messages)


def get_cat_fact():
    with open("content/cats.txt", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return random.choice(words)


def ball8():
    messages = {
        'positive': [
            'определённо да YEPPERS',
            'можешь быть уверен в этом YEPPERS',
            'никаких сомнений YEPPERS',
            'абсолютли YEPPERS',
            'ну естественно YEPPERS',
            'да YEPPERS'
        ],
        'probably': [
            'хорошие шансы Nice',
            'вероятнее всего Nice',
            'думаю, что да Nice',
            'не исключено Nice',
            'немаловероятно Nice'
        ],
        'uncertainly': [
            'пока не ясно think',
            'не уверен think',
            'тут всё не так однозначно think',
            'скажу за небольшую сумму MONEY',
            'не стоит вскрывать эту тему think',
            'может, @${random.chatter} знает точно? think',
            'спроси у @${random.chatter} think'
        ],
        'improbably': [
            'да нет, наверное heh',
            'шансы не очень heh',
            'скорее нет, чем да heh',
            'я бы не надеялся heh'
        ],
        'negative': [
            'даже не надейся NOPERS',
            'весьма сомнительно NOPERS',
            'определённо нет NOPERS',
            'вероятность КРАЙНЕ мала NOPERS',
            'никогда в жизни NOPERS',
            'нет, просто нет NOPERS'
        ]
    }
    random_key = random.choice(list(messages.keys()))
    random_message = random.choice(messages[random_key])

    return random_message


def get_iq():
    # Определим диапазоны и их веса
    iq_ranges = {
        1: (['Поздравляем, у вас 0! iq', '69 MHMM', '89 pivo', '228 TORCH', '322  rukopojatie',
            '365, прямо как дней в году! EarthDay', '666 - да вы сам дьявол! devil', '777 - джекпот GAMBA',
            'Мильон лишнего ику! umni', 'Бесконечность, ваш разум шире космоса! space'], ''),
        5: (range(1, 69), 'Dumb'),
        14: (range(70, 89), 'denied'),
        50: (range(90, 120), 'ymom'),
        20: (range(120, 150), 'pepeBigBrain'),
        10: (range(150, 201), 'GalaxyBrain')
    }

    random_range, emote = random.choices(list(iq_ranges.values()), weights=list(iq_ranges.keys()))[0]
    random_iq = random.choice(list(random_range))
    return f'У вас... {random_iq} {emote}'