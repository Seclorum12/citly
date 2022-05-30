from flask import Blueprint, Flask
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from typing import Type

from utils.api import ApiResource


class API:
    def __init__(self, app: Flask):
        self._app = app
        self._bp = Blueprint('api', __name__, url_prefix='/api')
        self._api = Api(self._bp)
        self._update_app_config()
        self._register_api_blueprint()
        self._docs = FlaskApiSpec(self._app)

    def _update_app_config(self):
        self._app.config.update({
            'APISPEC_SPEC': APISpec(
                title='Citly API',
                version='v1',
                plugins=[MarshmallowPlugin()],
                openapi_version='2.0.0'
            ),
            'APISPEC_SWAGGER_URL': '/api/swagger-raw/',  # URI to access API Doc JSON
            'APISPEC_SWAGGER_UI_URL': '/api/swagger/'  # URI to access UI of API Doc
        })

    def _register_api_blueprint(self):
        self._app.register_blueprint(self._bp)

    def add_resource_with_doc(self, resource: Type[ApiResource], url):
        self._api.add_resource(resource, url)
        self._docs.register(resource, blueprint=self._bp.name)
