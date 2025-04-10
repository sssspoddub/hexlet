import math


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


def make(numer, denom):
    a = math.gcd(numer, denom)
    return f"{numer // a}/{denom // a}"


def get_numer(number):
    numer, _ = number.split('/')
    return int(numer)


def get_denom(number):
    _, denom = number.split('/')
    return int(denom)


def add(number1, number2):
    numer1, denom1 = number1.split('/')
    numer2, denom2 = number2.split('/')

    numer1, denom1 = int(numer1), int(denom1)
    numer2, denom2 = int(numer2), int(denom2)

    new_numer = numer1 * denom2 + numer2 * denom1
    new_denom = denom1 * denom2

    return make(new_numer, new_denom)


def sub(number1, number2):
    numer1, denom1 = number1.split('/')
    numer2, denom2 = number2.split('/')

    numer1, denom1 = int(numer1), int(denom1)
    numer2, denom2 = int(numer2), int(denom2)

    new_numer = numer1 * denom2 - numer2 * denom1
    new_denom = denom1 * denom2

    return make(new_numer, new_denom)
