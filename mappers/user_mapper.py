

from models.models import User  
from helpers.user_helper import UserHelper  
from uuid import UUID

def models_to_helper(user_model: User) -> UserHelper:
    """
    Converts a User model instance to a UserHelper instance.
    """
    return UserHelper(
        id=user_model.id,
        phonenumber=user_model.phonenumber,
        name=user_model.name,
        password_hash=user_model.password_hash,
        role=user_model.role
    )

def helpers_to_model(user_helper: UserHelper) -> User:
    """
    Converts a UserHelper instance to a User model instance.
    """
    return User(
        id=user_helper.id,
        phonenumber=user_helper.phonenumber,
        name=user_helper.name,
        password_hash=user_helper.password_hash,
        role=user_helper.role
    )
