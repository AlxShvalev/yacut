import random
import string

from .models import URL_map


def get_random_string(length: int) -> str:
    """Генерирует случаюную строку из символов a-z, A-Z, 0-9 длины length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def get_unique_short_id(length: int) -> str:
    """Вызывает get_random_string пока не получит уникальное значение."""
    rand_string = get_random_string(length)
    while URL_map.query.filter_by(short=rand_string).first() is not None:
        rand_string = get_random_string(length)
    return rand_string
