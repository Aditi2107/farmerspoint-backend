

from repositories.farm_repository import (
    create_farm,
    find_farm_by_id,
    find_all_farms_by_farmer_id,
)
from services.country_service import get_or_create_country_service
from helpers.farm_helper import FarmHelper
from mappers.farm_mapper import helpers_to_model, models_to_helper

def create_farm_service(farm_data: dict):
    country = get_or_create_country_service("country_name")
    """Creates a farm using the provided data dictionary."""
    country_id=country.id
    print("country_id",country_id)
    farm_data ={"country_id":country_id,
            "area": farm_data["area"],
            "village": farm_data["village"],
            "crop_grown": farm_data["crop_grown"],
            "sowing_date": farm_data["sowing_date"],
            "farmer_id": farm_data["farmer_id"]}
    print("country id set",farm_data)

    farm_helper = FarmHelper.from_dict(farm_data)  
    farm_model = helpers_to_model(farm_helper)  
    created_farm = create_farm(farm_model)  
    return created_farm  

def get_farm_by_id(farm_id: int):
    """Retrieves a farm by its ID."""
    return find_farm_by_id(farm_id)  

def get_all_farms_by_farmer_id(farmer_id: int):
    """Retrieves all farms associated with a given farmer."""
    return find_all_farms_by_farmer_id(farmer_id)  

