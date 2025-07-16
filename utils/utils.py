from functools import wraps
from flask import session, jsonify

def login_required(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        if "usuario" not in session:
            return jsonify({"mensaje": "Debe iniciar sesión"}), 401
        return f(*args, **kwargs)
    return decorador
