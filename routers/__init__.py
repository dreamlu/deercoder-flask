# project/routes/__init__.py
from flask import Blueprint, jsonify

# Blueprint 中 ‘api’ https://segmentfault.com/q/1010000014300851
bp = Blueprint('api', __name__)
# 路由注册实例化user
from controllers.user import user


@bp.errorhandler(404)
def not_found(error):
    """
    :param error:不可少
    :return:
    """
    response = dict(status=404, msg="接口/数据不见啦(\'^\')")
    return jsonify(response), 404


def init_app(app):
    """
    注册路由-蓝图
    """
    app.register_blueprint(bp, url_prefix='/api')

# ...