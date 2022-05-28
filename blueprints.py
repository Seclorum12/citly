def register_all(app):
    from modules.core.controllers import core_bp
    app.register_blueprint(core_bp)
