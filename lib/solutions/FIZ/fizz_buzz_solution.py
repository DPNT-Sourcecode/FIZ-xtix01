# noinspection PyUnusedLocal
def deluxe(number):
    if ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 != 0:
        return 'fizz buzz fake deluxe'
    elif ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 == 0:
        return 'fizz buzz deluxe'
    else:
        return 'fizz buzz'

def fizz_deluxe(number):
    if ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 != 0:
        return 'fizz fake deluxe'
    if ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 == 0:
        return 'fizz deluxe'
    else:
        return 'fizz'

def buzz_deluxe(number):
    if ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 != 0:
        return 'buzz fake deluxe'
    if ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 == 0:
        return 'buzz deluxe'
    else:
        return 'buzz'

def fizz_buzz(number):
    if number%3==0 and number%5==0:
        return deluxe(number)
    elif '3' in str(number) and '5' in str(number):
        return deluxe(number)
    elif number%3==0 and '5' in str(number):
        return deluxe(number)
    elif number%5==0 and '3' in str(number):
        return deluxe(number)
    elif number%3==0 or '3' in str(number):
        return fizz_deluxe(number)
    elif number%5==0 or '5' in str(number):
        return buzz_deluxe( number)
    else:
        if ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 != 0:
            return 'fake deluxe'
        elif ((number%3==0 and '3' in str(number)) or  (number%5==0 and '5' in str(number))) and number%2 == 0:
            return 'deluxe'
        else:
            return number


