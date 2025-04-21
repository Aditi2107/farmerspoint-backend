

from flask import Blueprint, request, jsonify
from services.fertilizer_service import get_fertilizer_by_name, add_fertilizer, get_all_fertilizers

from middlewares.authentication import authenticate
from middlewares.authorization import authorization

fertilizer_bp = Blueprint("fertilizer", __name__)

@fertilizer_bp.route("/fertilizers", methods=["GET"])

def fetch_all_fertilizers():
    """Fetch all fertilizers."""
    try:
        fertilizers = get_all_fertilizers()
        return jsonify([fertilizer.to_dict() for fertilizer in fertilizers]), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch fertilizers", "details": str(e)}), 500

@fertilizer_bp.route("/create_fertilizer", methods=["POST"])

@authorization(["admin","super"])
def create_fertilizer():
    """Create a new fertilizer if it doesn't exist."""
    try:
        data = request.get_json()
        fertilizer_name = data.get("name")

        if not fertilizer_name:
            return jsonify({"error": "Fertilizer name is required"}), 400

        fertilizer = add_fertilizer(fertilizer_name)
        return jsonify(fertilizer.to_dict()), 201
    except Exception as e:
        return jsonify({"error": "Failed to create fertilizer", "details": str(e)}), 500

@fertilizer_bp.route("/fertilizers/<string:name>", methods=["GET"])

def fetch_fertilizer_by_name(name):
    """Fetch a fertilizer by name."""
    try:
        fertilizer = get_fertilizer_by_name(name)
        if not fertilizer:
            return jsonify({"error": "Fertilizer not found"}), 404

        return jsonify(fertilizer.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch fertilizer", "details": str(e)}), 500
