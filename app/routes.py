from flask import Blueprint, request, jsonify, current_app

from app import db
from app.models import Visitor

main = Blueprint('main', __name__)


@main.route('/')
def index():
    '''Index route.
    
    Returns the basic visitor info.
    '''

    ip = request.remote_addr

    visitor = Visitor.get_by_ip(ip)
    if not visitor:
        visitor = Visitor(
            ip=ip,
            user_agent=request.headers.get('User-Agent')
        )

        db.session.add(visitor)
        db.session.commit()

        current_app.logger.info(f'Added new visitor: <{visitor}>')

    return jsonify({
        'status': True,
        'ip': visitor.ip,
        'user-agent': visitor.user_agent
    })
