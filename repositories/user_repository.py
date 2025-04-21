

from models.models import User
from mappers.user_mapper import models_to_helper, helpers_to_model
from database import db  
import logging

logger = logging.getLogger(__name__)

def create_user(user_helper):
    """Creates a new user in the database."""
    try:
        print("inside create user",user_helper)
        user_model = helpers_to_model(user_helper)  
        db.session.add(user_model)
        db.session.commit()
        return models_to_helper(user_model)  
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating user: {str(e)}")
        return None

def find_user_by_id(user_id):
    """Finds a user by ID and returns it in UserHelper format."""
    try:
        user_model = db.session.query(User).filter_by(id=user_id).first()
        return models_to_helper(user_model) if user_model else None
    except Exception as e:
        logger.error(f"Error finding user by ID {user_id}: {str(e)}")
        return None

def find_user_by_name(name):
    """Finds a user by name and returns it in UserHelper format."""
    try:
        user_model = db.session.query(User).filter_by(name=name).first()
        return models_to_helper(user_model) if user_model else None
    except Exception as e:
        logger.error(f"Error finding user by name {name}: {str(e)}")
        return None
