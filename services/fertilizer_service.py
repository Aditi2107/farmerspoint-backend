

from repositories.fertilizer_repository import (
    find_fertilizer_by_name,
    create_fertilizer_by_name,
    find_all_fertilizers,
)
from helpers.fertilizer_helper import FertilizerHelper

def get_fertilizer_by_name(fertilizer_name):
    """Retrieve a fertilizer by name."""
    return find_fertilizer_by_name(fertilizer_name)

def add_fertilizer(fertilizer_name):
    """Add a new fertilizer if it does not already exist."""
    existing_fertilizer = find_fertilizer_by_name(fertilizer_name)
    if existing_fertilizer:
        return existing_fertilizer
    return create_fertilizer_by_name(fertilizer_name)

def get_all_fertilizers():
    """Retrieve all fertilizers."""
    return find_all_fertilizers()
