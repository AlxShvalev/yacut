from flask import abort, flash, redirect, request, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URL_map
from .utils import get_unique_short_id


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', form=URLForm()), 200


@app.route('/', methods=['POST'])
def create_id():
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data
        if short is None:
            short = get_unique_short_id(length=6)
        if URL_map.query.filter_by(short=short).first() is not None:
            flash(f'Имя {short} уже занято!')
            return redirect(url_for('index'))
        url = URL_map(
            original=original,
            short=short,
        )
        db.session.add(url)
        db.session.commit()
        short_link = request.host_url + short
        return render_template('index.html', form=form, url=short_link), 200
    return render_template('index.html', form=form), 200


@app.route('/<string:short_id>/')
def redirect_to_original_url(short_id: str):
    url = URL_map.query.filter_by(short=short_id).first()
    if url is None:
        return abort(404)
    return redirect(url.original, code=302)
