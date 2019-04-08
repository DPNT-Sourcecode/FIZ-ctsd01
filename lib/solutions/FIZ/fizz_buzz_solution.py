# noinspection PyUnusedLocal
import numpy as np

def fizz_buzz(number):
    digits = [int(d) for d in str(number)]
    deluxe = (number % 3 == 0 and 3 in digits) or (number % 5 == 0 and 5 in digits)

    if (number % 3 == 0 or 3 in digits) and (number % 5 == 0 or 5 in digits) and deluxe and (number % 2 != 0):
        return "fizz buzz fake deluxe"
    elif (number % 3 == 0 or 3 in digits) and (number % 5 == 0 or 5 in digits) and deluxe:
        return "fizz buzz deluxe"
    elif (number % 3 == 0 or 3 in digits) and (number % 5 == 0 or 5 in digits):
        return "fizz buzz"
    elif (number % 5 == 0 or 5 in digits) and deluxe and (number % 2 != 0):
        return "buzz fake deluxe"
    elif (number % 5 == 0 or 5 in digits) and deluxe:
        return "buzz deluxe"
    elif number % 5 == 0 or 5 in digits:
        return "buzz"
    elif (number % 3 == 0 or 3 in digits) and deluxe and (number % 2 != 0):
        return "fizz fake deluxe"
    elif (number % 3 == 0 or 3 in digits) and deluxe:
        return "fizz deluxe"
    elif number % 3 == 0 or 3 in digits:
        return "fizz"
    elif deluxe and (number % 2 != 0):
        return "fake deluxe"
    elif deluxe:
        return "deluxe"
    else:
        return number






# Remove deluxe
# put conditions in list/dict?
# should definitely do that!
                                        # deluxe = condition
                                        # fizz = condition
                                        #if fizz and deluxe:
                                        # return "fizz deluxe"






