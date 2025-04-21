from helpers.farmer_helper import FarmerHelper
from models.models import Farmer

def models_to_helper(farmer):
    """
    Convert Farmer model instance to FarmerHelper format.
    """
    if not farmer:
        return None
    return FarmerHelper(
        id=farmer.id,
        name=farmer.name,
        phonenumber=farmer.phonenumber,
        language=farmer.language,
        country_id=farmer.country_id
        
    )

def helpers_to_model(farmer_helper):
    """
    Convert FarmerHelper instance to Farmer model format.
    """
    if not farmer_helper:
        return None
    return Farmer(
        id=farmer_helper.id,
        name=farmer_helper.name,
        phonenumber=farmer_helper.phonenumber,
        language=farmer_helper.language,
        country_id=farmer_helper.country_id
        
    )
