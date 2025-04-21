

from flask import Blueprint, request, jsonify
from services.farm_service import (
    create_farm_service,
    get_farm_by_id,
    get_all_farms_by_farmer_id,
)
# from authentication import authenticate
from helpers.farm_helper import FarmHelper
from middlewares.authentication import authenticate
from middlewares.authorization import authorization

farm_bp = Blueprint("farm", __name__)

@farm_bp.route("/farm", methods=["POST"])

@authorization(["admin","super"])
def create_farm():
    """Creates a new farm."""
    try:
        farm_data = request.get_json()
        print("data",farm_data)
        

        created_farm = create_farm_service(farm_data)
        return jsonify({"success": True, "farm": created_farm.to_dict()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@farm_bp.route("/farm/<int:farm_id>", methods=["GET"])

def get_farm(farm_id):
    """Retrieves a farm by its ID."""
    farm = get_farm_by_id(farm_id)
    if not farm:
        return jsonify({"error": "Farm not found"}), 404
    return jsonify({"success": True, "farm": farm.to_dict()}), 200

@farm_bp.route("farmer/<int:farmer_id>/farms", methods=["GET"])

def get_farms_by_farmer(farmer_id):
    """Retrieves all farms associated with a given farmer."""
    farms = get_all_farms_by_farmer_id(farmer_id)
    return jsonify({"success": True, "farms": [farm.to_dict() for farm in farms]}), 200

