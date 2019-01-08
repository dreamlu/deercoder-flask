from flask import jsonify, request

from models import db

from models.models import User
from controllers.error import bad_request
from routers import bp


@bp.route('/users', methods=['GET'])
def get_users():
    # return "pong"
    limit = min(request.args.get('limit', 10, int), 100)
    offset = (request.args.get('page', 1, int) - 1) * request.args.get('limit', 10, int)
    return jsonify([user.to_dict() for user in User.query.limit(limit).offset(offset).all()])


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json() or {}
    if 'username' not in data:
        return bad_request('错误的参数')
    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'username' not in data:
        return bad_request('错误的参数')
    setattr(user, 'username', data['username'])
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'ok'})
