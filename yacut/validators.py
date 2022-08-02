import re
from typing import Optional

from .error_handlers import InvalidAPIUsage
from .utils import get_unique_short_id
from .models import URL_map


def custom_id_validator(custom_id: Optional[str]) -> str:
    if custom_id is None:
        custom_id = get_unique_short_id(length=6)
    if not re.match(r'^[a-zA-Z0-9]{,16}$', custom_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url_map = URL_map.query.filter_by(short=custom_id).first()
    if url_map:
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    return custom_id


def request_validator(data: Optional[dict]) -> dict:
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    return data


def url_validator(url: Optional[str]) -> str:
    if url is None:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    return url
