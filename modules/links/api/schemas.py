from marshmallow import Schema, fields


class LinkSchema(Schema):
    link = fields.Url(required=True, relative=False)
