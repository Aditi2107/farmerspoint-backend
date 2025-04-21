
from models.models import Schedule, Farm
from database import db
from sqlalchemy import select, func
import logging

logger = logging.getLogger(__name__)

def create_schedule(schedule: Schedule):
    """Creates a new schedule entry in the database."""
    try:
        db.session.add(schedule)
        db.session.commit()
        print("added in db",schedule)
        return schedule
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating schedule: {str(e)}")

def find_all_schedules_due_today_or_tomorrow(farm_id: int):
    """Finds all schedules that are due today or tomorrow for a given farm."""
    try:
        stmt = (
            select(Schedule)
            .join(Farm, Farm.id == Schedule.farm_id)
            .where(Farm.id == farm_id)
            .where((Schedule.days_after_sowing - (func.current_date() - Farm.sowing_date)).in_([0, 1]))
        )
        schedules = db.session.execute(stmt).scalars().all()
        return schedules if schedules else []
    except Exception as e:
        logger.error(f"Error finding schedules due today or tomorrow for farm {farm_id}: {e}")
        return []

def get_all_schedules_by_farm_id(farm_id: int):
    """Gets all schedules associated with a specific farm ID."""
    return db.session.query(Schedule).filter(Schedule.farm_id == farm_id).all()

def find_schedule_by_id(schedule_id: int):
    """Finds a schedule by its ID."""
    return db.session.query(Schedule).filter(Schedule.id == schedule_id).first()

def find_bill_for_one_farmer(farmer_id: int, farm_id: int):
    """Calculate the total bill for a specific farmer and farm."""
    try:
        stmt = (
            db.session.query(
                func.sum(Schedule.fertilizer_price * Schedule.quantity).label("total_amount"),
                Farm
            )
            .join(Farm, Farm.id == Schedule.farm_id)
            .where(Farm.farmer_id == farmer_id)
            .where(Farm.id == farm_id)
            .group_by(Farm.id)
        )
        bill = stmt.scalar()
        return bill
    except Exception as e:
        logger.error(f"Error calculating bill for farmer {farmer_id}, farm {farm_id}: {e}")
        return None
