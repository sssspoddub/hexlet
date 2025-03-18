import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def say_prime_or_not(number):
    if is_prime(number):
        print('yes')
    else:
        print('no')
