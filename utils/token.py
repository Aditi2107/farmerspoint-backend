import jwt
import os
from flask import current_app

def generate_token(name, user_id):
    print(os.getenv("SECRET_KEY"))
    print(f"Generating token for name: {name}, user_id: {user_id}")  # Debugging
    if not isinstance(name, str):
        raise ValueError("Expected a string value for name")
    """Generates a JWT token with the user's name and ID."""
    access_token = jwt.encode(
        {"name": name, "id": user_id},
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )
    return access_token

def decode_token(token):
    """Decodes and verifies a JWT token."""
    try:
        decoded_data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        return decoded_data
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
