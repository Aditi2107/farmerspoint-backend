

from flask import Blueprint, request, jsonify
from services.user_service import register_user, get_user_by_id, get_user_by_name , verify_password
from utils.token import generate_token
from middlewares.authentication import authenticate
from middlewares.authorization import authorization
from helpers.user_helper import UserHelper

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/register", methods=["POST"])

def register():
    """Registers a new regular user."""
    if request.method == "OPTIONS":
        # Respond to CORS preflight request
        response = ""
        response.status_code = 200
        return response
    try:
        user_data = request.get_json()
        print(user_data)
        # print(user_data["role"])
        # if "admin" in user_data.get("role", []):
        #     return jsonify("admin cannot create admin") 
        # elif "super" in user_data.get("role", []):
        #     return jsonify("admin cannot create super") 
         
        # else:
        role=['user']
        result = register_user(user_data,role)
            
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400  # User already exists

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route("/createsuper", methods=["POST"])

@authorization(["super"])  
def create_super():
     
    try:
        user_data = request.get_json()
        # user_data["role"] = "super"  
        role=['super']
        result = register_user(user_data,role)
        
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400  # User already exists

        return jsonify({"message": "super user created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route("/createadmin", methods=["POST"])

@authorization(["super"])  
def create_admin():
    
    try:
        user_data = request.get_json()
        role=['admin'] 
        
        result = register_user(user_data,role)
        
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400  # User already exists

        return jsonify({"message": "Admin created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route("/<int:user_id>", methods=["GET"])

def get_user(user_id):
    """Fetches a user by ID."""
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/name/<string:name>", methods=["GET"])

def get_user_by_name_view(name):
    """Fetches a user by name."""
    user = get_user_by_name(name)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/login", methods=["POST"])
def login():
    """Authenticates a user and returns a JWT token."""
    try:
        data = request.get_json()
        field_list = ["name", "password"]
        
        
        if not all(key in data for key in field_list):
            return jsonify({"error": "Missing required fields"}), 400

        name, password = data["name"], data["password"]

        
        user = get_user_by_name(name)
        if not user:
            return jsonify({"error": "No user"}), 401
            print({"no user"})

        
        if not verify_password(password, user.password_hash):
            return jsonify({"error": "Invalid credentials"}), 401

        
        access_token = generate_token(user.name, user.id)

        
        user_helper = UserHelper(id=user.id,name=user.name,password_hash=user.password_hash,role=user.role, phonenumber=user.phonenumber)

        
        return jsonify({
            "message": "Login successful",
            "user": user_helper.to_dict(),
            "access_token": access_token
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500