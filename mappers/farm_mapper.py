from helpers.farm_helper import FarmHelper
from models.models import Farm

def models_to_helper(farm: Farm) -> FarmHelper:
    """Converts a Farm model instance to a FarmHelper object."""
    if not farm:
        return None
    
    return FarmHelper(
        id=farm.id,
        country_id=farm.country_id,
        farmer_id=farm.farmer_id,
        area=farm.area,
        village=farm.village,
        crop_grown=farm.crop_grown,
        sowing_date=farm.sowing_date
    )

def helpers_to_model(farm_helper: FarmHelper) -> Farm:
    """Converts a FarmHelper object to a Farm model instance."""
    return Farm(
        country_id=farm_helper.country_id,
        farmer_id=farm_helper.farmer_id,
        area=farm_helper.area,
        village=farm_helper.village,
        crop_grown=farm_helper.crop_grown,
        sowing_date=farm_helper.sowing_date
    )
