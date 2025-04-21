

from flask import Blueprint, request, jsonify
from services.farmer_service import (
    create_farmer_user_service, 
    get_farmer_service_by_phone_or_name, 
    get_all_farmers_growing_crop, 
    get_all_farmers_service
)
from utils.validation import validate_required_fields
from middlewares.authentication import authenticate
from middlewares.authorization import authorization

farmer_bp = Blueprint("farmer_bp", __name__)

@farmer_bp.route("/create_farmer", methods=['POST'])

@authorization(["admin","super"])
def create_farmer():
    try:
        data = request.get_json()
        field_list = ["name", "phonenumber", "language", "country"]
        
        errors = validate_required_fields(data, field_list)
        if errors:
            return jsonify({"errors": errors}), 400
        
        name, phonenumber, language, country = [data[key] for key in field_list]
        
        farmer = get_farmer_service_by_phone_or_name(phonenumber, name)
        if farmer is not None:
            return jsonify({"error": "Farmer with this name or phone number already exists"}), 400

        new_farmer = create_farmer_user_service(name, phonenumber, language, country)
        return jsonify({"message": "Farmer created successfully!", "farmer": new_farmer}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@farmer_bp.route("/get_farmers_growing_crop", methods=["GET"])

def get_farmers_growing_crop():
    try:
        farmers = get_all_farmers_growing_crop()
        return jsonify({"farmers": farmers}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@farmer_bp.route("/get_all_farmers", methods=["GET"])

def get_all_farmers():
    try:
        farmers = get_all_farmers_service()
        return jsonify({"farmers": farmers}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
