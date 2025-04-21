

from functools import wraps
from flask import request, jsonify, current_app
import jwt 
from services.user_service import get_user_by_id

def authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Authentication token is missing"}), 401

        
        if token.startswith("Bearer "):
            token = token.split(" ")[1]  

        try:
            secret_key = current_app.config.get("SECRET_KEY")
            if not secret_key:
                return jsonify({"error": "Server misconfiguration: SECRET_KEY is missing"}), 500

            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            current_user = get_user_by_id(user_id=data.get("id"))

            if not current_user:
                return jsonify({"error": "Invalid authentication token"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        except Exception as e:
            return jsonify({"error": "Something went wrong", "details": str(e)}), 500

        return func(current_user, *args, **kwargs)

    return decorated
