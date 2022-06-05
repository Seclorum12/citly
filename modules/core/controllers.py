from flask import Blueprint, render_template, abort, request, redirect

from modules.links.services import LinksService

core_bp = Blueprint('core', __name__)


@core_bp.route('/')
def index():
    return render_template('index.html')


@core_bp.route('/<generated_link>')
def follow_link(generated_link):
    link = LinksService().follow(generated_link)
    if not link:
        abort(404)
    return redirect(link.original_link)
