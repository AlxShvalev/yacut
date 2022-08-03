from flask import abort, flash, redirect, request, render_template, typing
from http import HTTPStatus

from . import app, db, SHORT_LINK_LEN
from .forms import URLForm
from .models import URL_map
from .utils import get_unique_short_id


@app.route('/', methods=['GET'])
def index() -> typing.ResponseReturnValue:
    return render_template('index.html', form=URLForm()), HTTPStatus.OK


@app.route('/', methods=['POST'])
def create_short_url_view() -> typing.ResponseReturnValue:
    """Создает новое сокращение в базе."""
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data
        if short is None:
            short = get_unique_short_id(SHORT_LINK_LEN)
        if URL_map.query.filter_by(short=short).first() is not None:
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form), HTTPStatus.OK
        url = URL_map(
            original=original,
            short=short,
        )
        db.session.add(url)
        db.session.commit()
        short_link = request.host_url + short
        return (render_template('index.html', form=form, url=short_link),
                HTTPStatus.OK)
    return render_template('index.html', form=form), HTTPStatus.OK


@app.route('/<string:short_id>', methods=['GET'])
def get_original_url_view(short_id: str) -> typing.ResponseReturnValue:
    """Перенапраялвет на оригинальный URL по короткому"""
    url_map = URL_map.query.filter_by(short=short_id).first()
    if url_map is not None:
        return redirect(url_map.original, code=HTTPStatus.FOUND)
    abort(HTTPStatus.NOT_FOUND)
