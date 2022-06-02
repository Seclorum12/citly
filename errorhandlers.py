from flask import render_template, jsonify
from webargs.flaskparser import parser, abort


def page_not_found(e):
    return render_template('404.html'), 404


# This error handler is necessary for usage with Flask-RESTful
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    abort(400, errors=err.messages['json'])


def register_all(app):
    app.register_error_handler(404, page_not_found)
    parser.error_handler(handle_request_parsing_error)
