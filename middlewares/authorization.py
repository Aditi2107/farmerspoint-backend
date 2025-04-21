from functools import wraps
from flask import jsonify, request, current_app
from services.user_service import get_user_by_id
import jwt

def authorization(required_role):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify({"error": "Authentication token is missing"}), 401

            try:
                
                data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
                # current_user = get_user_by_id(user_id=data.get("id"))
                # print(current_user)
                # if not current_user:
                #     return jsonify({"error": "Invalid authentication token"}), 401

                # current_role = current_user.role
                current_role = request.headers.get("role")
                # current_role = getattr(current_user, "role", None) 
                print("current role", current_role, type(current_role))
                print("required role", required_role,type(current_role))
                if current_role not in required_role:
                    return jsonify({"error": "Unauthorized"}), 403

            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Invalid token"}), 401
            except Exception as e:
                return jsonify({"error": "Something went wrong", "details": str(e)}), 500

            return func(*args, **kwargs)

        return decorated

    return decorator
