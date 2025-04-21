

from repositories.schedule_repository import (
    create_schedule,
    find_all_schedules_due_today_or_tomorrow,
    get_all_schedules_by_farm_id,
    find_schedule_by_id,
    find_bill_for_one_farmer
)
from mappers.schedule_mapper import models_to_helper, helpers_to_model
import logging

logger = logging.getLogger(__name__)

def add_schedule(schedule_helper):
    """Adds a new schedule after converting it to a model instance."""
    try:
        schedule = helpers_to_model(schedule_helper)
        print("converted helper to model ")
        created_schedule = create_schedule(schedule)
        return models_to_helper(created_schedule)
    except Exception as e:
        logger.error(f"Error adding schedule: {e}")
        raise Exception("Failed to add schedule.")

def get_schedules_due_today_or_tomorrow(farm_id):
    """Retrieves schedules that are due today or tomorrow."""
    schedules = find_all_schedules_due_today_or_tomorrow(farm_id)
    return [models_to_helper(schedule) for schedule in schedules] if schedules else []

def get_schedules_by_farm_id(farm_id):
    """Retrieves all schedules for a given farm ID."""
    schedules = get_all_schedules_by_farm_id(farm_id)
    return [models_to_helper(schedule) for schedule in schedules] if schedules else []

def get_schedule_by_id(schedule_id):
    """Finds and returns a schedule by its ID."""
    schedule = find_schedule_by_id(schedule_id)
    return models_to_helper(schedule) if schedule else None

def get_bill_for_farmer(farmer_id, farm_id):
    """Calculates the total bill for a farmer based on farm schedules."""
    return find_bill_for_one_farmer(farmer_id, farm_id)


