from flask import flash, request, render_template

from . import app, db
from .forms import URLForm
from .models import URL_map
from .utils import generate_rand_string


@app.route('/', methods=['GET'])
def index():
    return render_template('yacut.html', form=URLForm())



@app.route('/', methods=['POST'])
def get_unique_short_id():
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data
        if short == '':
            short = generate_rand_string(6)
            while URL_map.query.filter_by(short=short).first() is not None:
                short = generate_rand_string(6)
        if URL_map.query.filter_by(short=short).first() is not None:
            flash('Это сокращение уже использовано для другой ссылки')
            return render_template('yacut.html', form=form)
        url = URL_map(
            original=original,
            short=short,
        )
        db.session.add(url)
        db.session.commit()
        host = request.host_url
        flash(f'Ваша новая ссылка готова: {host}{short}')
        return render_template('yacut.html', form=form, url=url)
    return render_template('yacut.html', form=form)
