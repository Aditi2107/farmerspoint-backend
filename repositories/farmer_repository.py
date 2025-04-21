

from models.models import Farmer,Farm
from sqlalchemy import or_, select
from database import db

def create_farmer(farmer):
    try:
        db.session.add(farmer)
        db.session.commit()
        return farmer
    except Exception as e:
        db_session.rollback()
        raise Exception(f"Error creating farmer: {str(e)}")

def find_farmer_by_phone_or_name(phonenumber, name):
    return db.session.query(Farmer).filter(
        (Farmer.phonenumber == phonenumber) | (Farmer.name == name)
    ).first()

def find_all_farmers_growing_crop():
    stmt = select(Farmer).join(Farm, Farmer.id == Farm.farmer_id)  
    farmers = db.session.execute(stmt).scalars().all()
    return farmers

def find_farmer_by_id(farmer_id):
    return db.session.query(Farmer).filter(Farmer.id == farmer_id).first()

def find_all_farmers():
    return db.session.query(Farmer).all()
