

from services.country_service import get_or_create_country_service
from repositories.farmer_repository import (
    find_all_farmers_growing_crop,
    find_farmer_by_phone_or_name,
    find_farmer_by_id,
    find_all_farmers,
    create_farmer
)
from mappers.farmer_mapper import models_to_helper, helpers_to_model
from helpers.farmer_helper import FarmerHelper

def create_farmer_user_service(name, phonenumber, language, country):
    try:
        country = get_or_create_country_service(country)
        farmer_data = {
            "name": name,
            "phonenumber": phonenumber,
            "language": language,
            "country_id": country.id
        }
        
        farmer_helper = FarmerHelper.from_dict(farmer_data)  
        farmer_model = helpers_to_model(farmer_helper)  

        saved_farmer = create_farmer(farmer_model) 
        return models_to_helper(saved_farmer).to_dict()  
    except Exception as e:
        raise Exception(f"Error in create_farmer_user_service: {str(e)}")

def get_farmer_service_by_phone_or_name(phonenumber, name):
    farmer = find_farmer_by_phone_or_name(str(phonenumber).strip(), str(name).strip().lower())
    return models_to_helper(farmer).to_dict() if farmer else None

def get_all_farmers_growing_crop():
    farmers = find_all_farmers_growing_crop()
    return [models_to_helper(farmer).to_dict() for farmer in farmers] if farmers else []

def find_farmer_by_id_service(farmer_id):
    farmer = find_farmer_by_id(farmer_id)
    return models_to_helper(farmer).to_dict() if farmer else None

def get_all_farmers_service():
    farmers = find_all_farmers()
    return [models_to_helper(farmer).to_dict() for farmer in farmers] if farmers else []


