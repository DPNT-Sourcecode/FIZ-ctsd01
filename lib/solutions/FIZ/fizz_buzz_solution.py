# noinspection PyUnusedLocal
def fizz_buzz(number):
    digits = [int(d) for d in str(number)]
    if (number % 3 == 0 or 3 in digits) and (number % 5 == 0 or 5 in digits):
        return "fizz buzz"
    elif number % 5 == 0 or 5 in digits:
        return "buzz"
    elif number % 3 == 0 or 3 in digits:
        return "fizz"
    else:
        return number



