from flask import make_response, jsonify

from __init__ import create_app


app = create_app()


@app.route('/')
def index():
    return "pong"


# @app.errorhandler(404)
# def not_found():
#     response = dict(status=0, message="404 Not Found")
#     return jsonify({
#         'msg': '接口不见啦(\'^\')',
#         'status': 404,
#     }), 404

#
# if __name__== '__main__':
#     app.run(
#         hos='0.0.0.0',
#         port=6000,
#         debug=True
#     )
