

from models.models import Fertilizer
from database import db
from sqlalchemy.exc import SQLAlchemyError
from mappers.fertilizer_mapper import models_to_helper

def find_fertilizer_by_name(fertilizer_name):
    """Find a fertilizer by its name and return it in helper format."""
    fertilizer = db.session.query(Fertilizer).filter(Fertilizer.fertilizer_name == fertilizer_name).first()
    return models_to_helper(fertilizer)

def create_fertilizer_by_name(fertilizer_name):
    """Create a new fertilizer entry and return it in helper format."""
    try:
        new_fertilizer = Fertilizer(fertilizer_name=fertilizer_name)
        db.session.add(new_fertilizer)
        db.session.commit()
        return models_to_helper(new_fertilizer)
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Error creating fertilizer: {str(e)}")

def find_all_fertilizers():
    """Retrieve all fertilizers and return them in helper format."""
    fertilizers = db.session.query(Fertilizer).all()
    return [models_to_helper(fertilizer) for fertilizer in fertilizers]
