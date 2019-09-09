from flask import Blueprint, render_template

bp_web = Blueprint('BP Web', __name__)

@bp_web.route('/')
def index():
    return render_template('index.html')