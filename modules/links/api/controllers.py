from flask import request
from flask_apispec import marshal_with, use_kwargs, doc
from utils.api import ApiResource
from .schemas import ForeignLinkSchema


class MakeShortLink(ApiResource):
    @use_kwargs(ForeignLinkSchema)
    @marshal_with(ForeignLinkSchema)
    def post(self, **kwargs):
        print(request.json)
        return 200
