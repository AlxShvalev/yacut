from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .validators import custom_id_validator, request_validator, url_validator


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request_validator(request.get_json())
    original = url_validator(data.get('url'))
    short = custom_id_validator(data.get('custom_id'))
    data = dict(original=original, short=short)
    url = URL_map()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route('/api/id/<string:short_id>/')
def get_url(short_id):
    url = URL_map.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(url.get_original_url()), 200
