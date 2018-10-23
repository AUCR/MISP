# coding=utf-8
from flask import Blueprint, render_template
from flask_login import login_required

misp_page = Blueprint('misp', __name__, template_folder='templates')


@misp_page.route('/misp')
@login_required
def misp_route():
    """MiSP default rule view."""
    return render_template('misp.html')
