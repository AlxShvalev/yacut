import re
from typing import Optional

from . import SHORT_LINK_LEN, SHORT_LINK_TEMPLATE
from .error_handlers import InvalidAPIUsage
from .utils import get_unique_short_id
from .models import URL_map


def custom_id_validator(custom_id: Optional[str]) -> str:
    """Валидация поля custom_id API запроса."""
    if custom_id is None:
        custom_id = get_unique_short_id(SHORT_LINK_LEN)
    if not re.match(SHORT_LINK_TEMPLATE, custom_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url_map = URL_map.query.filter_by(short=custom_id).first()
    if url_map:
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    return custom_id


def request_validator(data: Optional[dict]) -> dict:
    """Валидация API запроса."""
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    return data


def url_validator(url: Optional[str]) -> str:
    """Валидация поля url API запроса."""
    if url is None:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    return url
