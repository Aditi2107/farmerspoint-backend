from models.models import Country
from helpers.country_helper import CountryHelper
from database import db
import logging


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def find_one_country(country_name):
    """Find a country by name."""
    try:
        country = Country.query.filter_by(country_name=country_name).first()
        print("already created country",country)
        return country
        #return country.to_dict() if country else None
    except Exception as e:
        logger.error(f"Error finding country: {e}")
        return None

def create_one_country(country_name):
    """Create a new country entry in the database."""
    try:
        country = Country(country_name=country_name)
        db.session.add(country)
        db.session.commit()
        return country
        # return country.to_dict()
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating country: {e}")
        return None
