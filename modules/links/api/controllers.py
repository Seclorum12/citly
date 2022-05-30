from flask import request
from flask_apispec import marshal_with, use_kwargs, doc

from utils.api import ApiResource
from .schemas import LinkSchema


class MakeShortLink(ApiResource):
    @use_kwargs(LinkSchema)
    @marshal_with(LinkSchema)
    def post(self, **kwargs):
        print(request.json)
        return 200
