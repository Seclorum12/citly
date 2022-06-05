from flask import jsonify, request
from flask_apispec import marshal_with, use_kwargs

from utils.api import ApiResource
from .schemas import RequestForeignLinkSchema
from ..services import LinksService


class MakeShortLink(ApiResource):
    def __init__(self):
        self.link_service = LinksService()

    @use_kwargs(RequestForeignLinkSchema)
    @marshal_with(RequestForeignLinkSchema)
    def post(self, **kwargs):
        original_link = kwargs.get('link')
        link, is_created = self.link_service.get_or_generate_short_link(original_link)
        return jsonify({
            'is_created': is_created,
            'generated_link': link.generated_link,
            'short_link': f'{request.host_url}{link.generated_link}',
            'follows': link.follows
        })
