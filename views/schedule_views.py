

from flask import Blueprint, request, jsonify
from services.schedule_service import (
    add_schedule,
    get_schedules_due_today_or_tomorrow,
    get_schedules_by_farm_id,
    get_schedule_by_id,
    get_bill_for_farmer
)
from helpers.schedule_helper import ScheduleHelper
import logging
from middlewares.authentication import authenticate
from middlewares.authorization import authorization

logger = logging.getLogger(__name__)

schedule_bp = Blueprint("schedule", __name__)

@schedule_bp.route("/create_schedule", methods=["POST"])

@authorization(["admin","super"])
def create_schedule():
    """Endpoint to create a new schedule."""
    try:
        data = request.get_json()
        schedule_helper = ScheduleHelper.from_dict(data)
        print("schedulehelper created")
        created_schedule = add_schedule(schedule_helper)
        return jsonify(created_schedule.to_dict()), 201
    except Exception as e:
        logger.error(f"Error creating schedule: {e}")
        return jsonify({"error": "Failed to create schedule"}), 400

@schedule_bp.route("/schedules/<int:schedule_id>", methods=["GET"])

def fetch_schedule_by_id(schedule_id):
    """Fetch a schedule by its ID."""
    schedule = get_schedule_by_id(schedule_id)
    if schedule:
        return jsonify(schedule.to_dict()), 200
    return jsonify({"error": "Schedule not found"}), 404

@schedule_bp.route("/schedules/due/<int:farm_id>", methods=["GET"])

def fetch_schedules_due_today_or_tomorrow(farm_id):
    """Fetch all schedules due today or tomorrow for a given farm."""
    schedules = get_schedules_due_today_or_tomorrow(farm_id)
    return jsonify([schedule.to_dict() for schedule in schedules]), 200

@schedule_bp.route("/schedules/farm/<int:farm_id>", methods=["GET"])

def fetch_schedules_by_farm(farm_id):
    """Fetch all schedules for a given farm ID."""
    schedules = get_schedules_by_farm_id(farm_id)
    return jsonify([schedule.to_dict() for schedule in schedules]), 200

@schedule_bp.route("/schedules/bill/<int:farmer_id>/<int:farm_id>", methods=["GET"])

def fetch_bill_for_farmer(farmer_id, farm_id):
    """Fetch the total bill for a farmer's farm."""
    bill = get_bill_for_farmer(farmer_id, farm_id)
    if bill:
        return jsonify({"total_bill": float(bill)}), 200
    return jsonify({"error": "No bill found"}), 404

