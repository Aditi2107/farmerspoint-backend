# from models.models import db, Farm

# class FarmRepository:
#     @staticmethod
#     def create_farm(area, village, crop_grown, sowing_date, farmer_id, country_id):
#         """Create a new farm entry with country ID."""
#         try:
#             farm = Farm(
#                 area=area, 
#                 village=village, 
#                 crop_grown=crop_grown, 
#                 sowing_date=sowing_date, 
#                 farmer_id=farmer_id,
#                 country_id=country_id 
#             )
#             db.session.add(farm)
#             db.session.commit()
#             return farm
#         except Exception as e:
#             db.session.rollback()
#             print(f"Error creating farm: {e}")
#             return None

#     @staticmethod
#     def find_farm_by_id(farm_id):
#         """Find a farm by its ID."""
#         try:
#             return Farm.query.get(farm_id)
#         except Exception as e:
#             print(f"Error finding farm by ID: {e}")
#             return None

#     @staticmethod
#     def find_all_farms_by_farmer_id(farmer_id):
#         """Find all farms belonging to a farmer by farmer ID."""
#         try:
#             return Farm.query.filter_by(farmer_id=farmer_id).all()
#         except Exception as e:
#             print(f"Error finding farms for farmer ID {farmer_id}: {e}")
#             return []

#     @staticmethod
#     def find_all_farms_by_country_id(country_id):
#         """Find all farms in a specific country."""
#         try:
#             return Farm.query.filter_by(country_id=country_id).all()
#         except Exception as e:
#             print(f"Error finding farms for country ID {country_id}: {e}")
#             return []

# from models import Farm
# from database import db
# import logging

# # Configure logging
# logging.basicConfig(level=logging.ERROR)
# logger = logging.getLogger(__name__)

# def create_farm(country_id, area, village, crop_grown, sowing_date, farmer_id):
#     """Create a new farm and store it in the database."""
#     try:
#         farm = Farm(
#             area=area,
#             village=village,
#             country_id=country_id,
#             farmer_id=farmer_id,
#             crop_grown=crop_grown,
#             sowing_date=sowing_date
#         )
#         db.session.add(farm)
#         db.session.commit()
#         return farm
#     except Exception as e:
#         db.session.rollback()
#         logger.error(f"Error creating farm: {e}")
#         return None
    
# def find_one_farm(farm_id):
#     """Find a farm by its ID."""
#     try:
#         return Farm.query.get(farm_id)
#     except Exception as e:
#         logger.error(f"Error finding farm by ID: {e}")
#         return None
        
# def find_all_farms_of_farmer(farmer_id):
#     """Find all farms owned by a specific farmer."""
#     try:
#         farms = Farm.query.filter_by(farmer_id=farmer_id).all()
#         return farms
#     except Exception as e:
#         logger.error(f"Error finding farms for farmer {farmer_id}: {e}")
#         return []
# from models.models import Farm
# from database import db
# import logging

# # Configure logging
# logging.basicConfig(level=logging.ERROR)
# logger = logging.getLogger(__name__)

# def create_farm(country_id, area, village, crop_grown, sowing_date, farmer_id):
#     """Create a new farm and store it in the database."""
#     try:
#         farm = Farm(area=area,village=village,country_id=country_id,farmer_id=farmer_id,crop_grown=crop_grown,sowing_date=sowing_date)
#         db.session.add(farm)
#         db.session.commit()
#         print("farm created")
#         return farm.to_dict()
#     except Exception as e:
#         db.session.rollback()
#         logger.error(f"Error creating farm: {e}")
#         return None
    
# def find_one_farm(farm_id):
#     """Find a farm by its ID."""
#     try:
#         farm = Farm.query.get(farm_id)
#         return farm.to_dict() if farm else None
#     except Exception as e:
#         logger.error(f"Error finding farm by ID {farm_id}: {e}")
#         return None
        
# def find_all_farms_of_farmer(farmer_id):
#     """Find all farms owned by a specific farmer."""
#     try:
#         farms = Farm.query.filter_by(farmer_id=farmer_id).all()
#         return [farm.to_dict() for farm in farms] if farms else []
#     except Exception as e:
#         logger.error(f"Error finding farms for farmer {farmer_id}: {e}")
#         return []

from models.models import Farm
from database import db
from sqlalchemy import select
from mappers.farm_mapper import models_to_helper  

def create_farm(farm):
    """Creates a new farm entry in the database."""
    try:
        db.session.add(farm)
        db.session.commit()
        return models_to_helper(farm)  # Converting to helper before returning
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating farm: {str(e)}")

def find_farm_by_id(farm_id):
    """Finds a farm by its ID."""
    farm = db.session.query(Farm).filter(Farm.id == farm_id).first()
    return models_to_helper(farm) if farm else None  # Converting to helper format

def find_all_farms_by_farmer_id(farmer_id):
    """Finds all farms associated with a farmer."""
    stmt = select(Farm).where(Farm.farmer_id == farmer_id)
    farms = db.session.execute(stmt).scalars().all()
    return [models_to_helper(farm) for farm in farms] if farms else []  

def find_all_farms():
    return db.session.query(Farm).all()