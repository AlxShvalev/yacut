import random
import string

from .models import URL_map


def get_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def get_unique_short_id(length: int) -> str:
    rand_string = get_random_string(length)
    while URL_map.query.filter_by(short=rand_string).first() is not None:
        rand_string = get_random_string(length)
    return rand_string
