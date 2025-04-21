from helpers.schedule_helper import ScheduleHelper
from models.models import Schedule

def models_to_helper(schedule: Schedule) -> ScheduleHelper:
    """Converts a Schedule model instance to a ScheduleHelper instance."""
    return ScheduleHelper(
        id=schedule.id,
        days_after_sowing=schedule.days_after_sowing,
        quantity=schedule.quantity,
        quantity_unit=schedule.quantity_unit,
        fertilizer_price=schedule.fertilizer_price,
        fertilizer_id=schedule.fertilizer_id,
        farm_id=schedule.farm_id
    )

def helpers_to_model(schedule_helper: ScheduleHelper) -> Schedule:
    """Converts a ScheduleHelper instance to a Schedule model instance."""
    return Schedule(
        days_after_sowing=schedule_helper.days_after_sowing,
        quantity=schedule_helper.quantity,
        quantity_unit=schedule_helper.quantity_unit,
        fertilizer_price=schedule_helper.fertilizer_price,
        fertilizer_id=schedule_helper.fertilizer_id,
        farm_id=schedule_helper.farm_id
    )
