from helpers.fertilizer_helper import FertilizerHelper
from models.models import Fertilizer

def models_to_helper(fertilizer: Fertilizer) -> FertilizerHelper:
    """Convert a Fertilizer model object to a FertilizerHelper object."""
    if not fertilizer:
        return None
    return FertilizerHelper(
        id=fertilizer.id,
        fertilizer_name=fertilizer.fertilizer_name
    )

def helpers_to_model(helper: FertilizerHelper) -> Fertilizer:
    """Convert a FertilizerHelper object to a Fertilizer model object."""
    if not helper:
        return None
    return Fertilizer(
        id=helper.id,
        fertilizer_name=helper.fertilizer_name
    )
