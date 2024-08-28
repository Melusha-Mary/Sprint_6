from data import DataForOrder
import random


def choice_name():
    return random.choice(DataForOrder.NAME)


def choice_surname():
    return random.choice(DataForOrder.SURNAME)


def choice_address():
    return random.choice(DataForOrder.ADDRESSE)


def choice_station():
    return random.choice(DataForOrder.STATION)


def choice_phone():
    number = random.randint(1111111, 9999999)
    return f'8916{number}'


def choice_rental_period():
    return random.choice(DataForOrder.RENTAL_PERIOD)


def choice_color():
    return random.choice(DataForOrder.COLOR)


def choice_comment():
    return random.choice(DataForOrder.COMMENT)
