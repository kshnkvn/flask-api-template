from flask import Blueprint, jsonify

main = Blueprint('main', __name__)


@main.route('/')
def index():
    '''Index route.'''

    return jsonify({'status': True})
