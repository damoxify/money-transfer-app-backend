from flask import jsonify

def handle_bad_request(e):
    response = jsonify(error=str(e))
    response.status_code = 400
    return response

def handle_unauthorized(e):
    response = jsonify(error=str(e))
    response.status_code = 401
    return response

def handle_not_found(e):
    response = jsonify(error=str(e))
    response.status_code = 404
    return response

def handle_internal_server_error(e):
    response = jsonify(error=str(e))
    response.status_code = 500
    return response
