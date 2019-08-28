# noinspection PyUnusedLocal
def deluxe(num_len, number):
    if num_len == 1 and number > 10 and number%2 != 0:
        return 'fizz buzz fake deluxe'
    elif num_len == 1 and number > 10 and number%2 == 0:
        return 'fizz buzz deluxe'
    else:
        return 'fizz buzz'

def fizz_deluxe(num_len, number):
    if num_len == 1 and number > 10 and number%2 != 0:
        return 'fizz fake deluxe'
    if num_len == 1 and number > 10 and number%2 == 0:
        return 'fizz deluxe'
    else:
        return 'fizz'

def buzz_deluxe(num_len, number):
    if num_len == 1 and number > 10 and number%2 != 0:
        return 'buzz fake deluxe'
    if num_len == 1 and number > 10 and number%2 == 0:
        return 'buzz deluxe'
    else:
        return 'buzz'

def fizz_buzz(number):
    num_len = len(set(list(str(number))))
    if number%3==0 and number%5==0:
        return deluxe(num_len, number)
    elif '3' in str(number) and '5' in str(number):
        return deluxe(num_len, number)
    elif number%3==0 and '5' in str(number):
        return deluxe(num_len, number)
    elif number%5==0 and '3' in str(number):
        return deluxe(num_len, number)
    elif number%3==0 or '3' in str(number):
        return fizz_deluxe(num_len, number)
    elif number%5==0 or '5' in str(number):
        return buzz_deluxe(num_len, number)
    else:
        if num_len == 1 and number>10 and number%2 != 0:
            return 'fake deluxe'
        elif num_len == 1 and number>10 and number%2 == 0:
            return 'deluxe'
        else:
            return number
