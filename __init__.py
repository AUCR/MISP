# coding=utf-8
from aucr_app.plugins.MISP.routes import misp_page
# TODO create models.py file
# from app.plugins.MISP import models


def load(app):
    """AUCR misp plugin flask app blueprint registration."""
    app.register_blueprint( misp_page   , url_prefix='/misp')
