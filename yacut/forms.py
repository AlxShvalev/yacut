from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from . import SHORT_LINK_TEMPLATE


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Значение должно быть валидной ссылкой'),
        ]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=16, message='Допустимая длина 16 символов.'),
            Regexp(
                SHORT_LINK_TEMPLATE,
                message=('Допустимые символы: '
                         'буквы латинского алфавита и цифры.')
            )
        ]
    )
    submit = SubmitField('Создать')
