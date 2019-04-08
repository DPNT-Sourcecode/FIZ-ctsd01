# noinspection PyUnusedLocal
import numpy as np

def fizz_buzz(number):
    digits = [int(d) for d in str(number)]
    if (number % 3 == 0 or 3 in digits) and (number % 5 == 0 or 5 in digits) and ((len(np.unique(digits)) == 1) and number > 10) and (number % 2 != 0):
        return "fizz buzz fake deluxe"
    elif (number % 3 == 0 or 3 in digits) and (number % 5 == 0 or 5 in digits) and ((len(np.unique(digits)) == 1) and number > 10):
        return "fizz buzz deluxe"
    elif (number % 3 == 0 or 3 in digits) and (number % 5 == 0 or 5 in digits):
        return "fizz buzz"
    elif (number % 5 == 0 or 5 in digits) and ((len(np.unique(digits)) == 1) and number > 10) and (number % 2 != 0):
        return "buzz fake deluxe"
    elif (number % 5 == 0 or 5 in digits) and ((len(np.unique(digits)) == 1) and number > 10):
        return "buzz deluxe"
    elif number % 5 == 0 or 5 in digits:
        return "buzz"
    elif (number % 3 == 0 or 3 in digits) and ((len(np.unique(digits)) == 1) and number > 10) and (number % 2 != 0):
        return "fizz fake deluxe"
    elif (number % 3 == 0 or 3 in digits) and ((len(np.unique(digits)) == 1) and number > 10):
        return "fizz deluxe"
    elif number % 3 == 0 or 3 in digits:
        return "fizz"
    elif len(np.unique(digits)) == 1 and number > 10 and (number % 2 != 0):
        return "fake deluxe"
    elif len(np.unique(digits)) == 1 and number > 10:
        return "deluxe"
    else:
        return number


# put conditions in list/dict?
# should definitely do that!



