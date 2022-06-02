from marshmallow import Schema, fields, ValidationError
from urllib.parse import urlparse
from flask import request


def validate_link_is_foreign(link):
    link = urlparse(link)
    if link.netloc == request.host:
        raise ValidationError('Citly url not allowed')


class ForeignLinkSchema(Schema):
    link = fields.Url(required=True, relative=False, validate=validate_link_is_foreign)
