from datetime import datetime
from flask import request

from yacut import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    _fields = ['original', 'short']

    def to_dict(self) -> dict:
        return dict(
            url=self.original,
            short_link=request.host_url + self.short,
        )

    def from_dict(self, data: dict) -> None:
        for field in self._fields:
            if field in data:
                setattr(self, field, data[field])

    def original_url_to_dict(self) -> dict:
        return dict(
            url=self.original
        )

    def get_short_url(self):
        return request.host_url + self.short
