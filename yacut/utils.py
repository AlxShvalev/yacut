import random
import string


def generate_rand_string(length):
    characters = string.ascii_letters + string.digits
    rand_string = ''.join(random.choices(characters, k=length))
    return rand_string
