from flask import Blueprint, jsonify

bp = Blueprint('mained', __name__)

@bp.route('/')
def index():
    return jsonify(text="json")
