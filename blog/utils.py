import random
import string


def get_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return return_str
