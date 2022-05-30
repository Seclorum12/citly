from api import API


def add_all(api: API):
    from modules.links.api.controllers import MakeShortLink
    api.add_resource_with_doc(MakeShortLink, '/make-short-link')
