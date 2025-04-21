

from repositories.user_repository import create_user, find_user_by_id, find_user_by_name
from helpers.user_helper import UserHelper
import logging
from werkzeug.security import check_password_hash,generate_password_hash
logger = logging.getLogger(__name__)

def register_user(user_data,role):
    """Registers a new user only if they don't already exist."""
    try:
        existing_user = find_user_by_name(user_data["name"])
        if existing_user:
            return {"error": "User with this name already exists"}

        
        hashed_password = generate_password_hash(user_data["password_hash"], method="pbkdf2:sha256")

        user_data["password_hash"] = hashed_password  
        print("above user helper ")
        
        user_helper = UserHelper(**user_data,role=role)  
        created_user = create_user(user_helper)
        return created_user
    except Exception as e:
        logger.error(f"Error registering user: {str(e)}")
        return None

def get_user_by_id(user_id):
    """Fetches a user by ID and returns it in UserHelper format."""
    try:
        return find_user_by_id(user_id)
    except Exception as e:
        logger.error(f"Error fetching user by ID {user_id}: {str(e)}")
        return None

def get_user_by_name(name):
    """Fetches a user by name and returns it in UserHelper format."""
    try:
        return find_user_by_name(name)
    except Exception as e:
        logger.error(f"Error fetching user by name {name}: {str(e)}")
        return None



def verify_password(provided_password, stored_password_hash):
    """Verifies if the provided password matches the hashed password."""
    return check_password_hash(stored_password_hash, provided_password)
