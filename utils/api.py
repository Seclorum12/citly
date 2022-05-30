from flask_apispec import MethodResource
from flask_restful import Resource


class ApiResource(MethodResource, Resource):
    pass
