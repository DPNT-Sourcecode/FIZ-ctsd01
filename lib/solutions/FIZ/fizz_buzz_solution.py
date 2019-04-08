# noinspection PyUnusedLocal
import numpy as np

def fizz_buzz(number):
    digits = [int(d) for d in str(number)]
    deluxe = (number % 3 == 0 and 3 in digits) or (number % 5 == 0 and 5 in digits)
    fake = (number % 2 != 0)
    fizz = (number % 3 == 0 or 3 in digits)
    buzz = (number % 5 == 0 or 5 in digits)

    if fizz and buzz and deluxe and fake:
        return "fizz buzz fake deluxe"
    elif fizz and buzz and deluxe:
        return "fizz buzz deluxe"
    elif fizz and buzz:
        return "fizz buzz"
    elif buzz and deluxe and fake:
        return "buzz fake deluxe"
    elif buzz and deluxe:
        return "buzz deluxe"
    elif buzz:
        return "buzz"
    elif fizz and deluxe and fake:
        return "fizz fake deluxe"
    elif fizz and deluxe:
        return "fizz deluxe"
    elif fizz:
        return "fizz"
    elif deluxe and fake:
        return "fake deluxe"
    elif deluxe:
        return "deluxe"
    else:
        return number
