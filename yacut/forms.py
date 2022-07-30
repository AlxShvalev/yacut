from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле')
        ]
    )
    short_link = URLField(
        'Ваш вариант короткой ссылки',
        validators=[Optional(), Length(6, 16)]
    )
    submit = SubmitField('Создать')
