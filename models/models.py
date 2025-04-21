
from database import db
import enum
from sqlalchemy import ARRAY, Enum
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum as PyEnum

class Country(db.Model, SerializerMixin):
    __tablename__ = "country"
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String, unique=True, nullable=False)
    farmers = db.relationship("Farmer", back_populates="country")
    farms = db.relationship("Farm", back_populates="country")
    def to_dict(self):
        """Convert the Country ORM object to a dictionary."""
        return {
            "id": self.id,
            "country_name": self.country_name
        }
    

class Farmer(db.Model, SerializerMixin):
    __tablename__ = "farmer"
    id = db.Column(db.Integer, primary_key=True)
    phonenumber = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    country_id = db.Column(db.Integer,db.ForeignKey(Country.id), nullable=False)
    language = db.Column(db.String, nullable=False)
    country = db.relationship("Country", back_populates="farmers")
    farms = db.relationship("Farm", back_populates="farmer")
    
    def to_dict(self):
        """Convert the Farmer ORM object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "phonenumber": self.phonenumber,
            "language": self.language,
            "country": self.country.to_dict() if self.country else None  
        }



class User(db.Model, SerializerMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phonenumber = db.Column(db.String(10),unique=True, nullable=False)
    name = db.Column(db.String,unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False) # user , super , admin 
    
    def set_password(self, password_hash):
        self.password_hash = generate_password_hash(password_hash)
    
    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)

class QuantityUnitEnum(enum.Enum):
    TON = "ton"
    KILOGRAM = "kg"
    GRAM = "g"
    LITRE = "l"
    MILLILITRE = "ml"

class Fertilizer(db.Model, SerializerMixin):
    __tablename__ = "fertilizer"
    id = db.Column(db.Integer, primary_key=True)
    fertilizer_name = db.Column(db.String, nullable=False, unique=True)

class Farm(db.Model, SerializerMixin):
    __tablename__ = "farm"
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.ForeignKey(Country.id), nullable=False)
    area = db.Column(db.String, nullable=False)
    village = db.Column(db.String, nullable=False)
    crop_grown = db.Column(db.String, nullable=False)
    sowing_date = db.Column(db.Date, nullable=False)
    farmer_id = db.Column(db.ForeignKey(Farmer.id), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"), nullable=False)
    farmer = db.relationship("Farmer", back_populates="farms")
    country = db.relationship("Country", back_populates="farms")
    schedules = db.relationship("Schedule", back_populates="farm")

    def to_dict(self):
        return {
            "id": self.id,
            "country_name": self.country.country_name,
            "area": self.area,
            "village": self.village,
            "crop_grown": self.crop_grown,
            "sowing_date": self.sowing_date,
            "farmer": self.farmer.name,
            "farmer_id": self.farmer.id
        }
    
 

class Schedule(db.Model, SerializerMixin):
    __tablename__ = "schedule"
    id = db.Column(db.Integer, primary_key=True)
    days_after_sowing = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    # quantity_unit = db.Column(Enum(QuantityUnitEnum, values_callable=lambda x: [e.value for e in x]), nullable=False)
    quantity_unit=db.Column(db.Enum(QuantityUnitEnum), nullable=False)
    fertilizer_id = db.Column(db.ForeignKey(Fertilizer.id), nullable=False)
    fertilizer_price = db.Column(db.Integer, nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    farm = db.relationship("Farm", back_populates="schedules")
    fertilizer = db.relationship("Fertilizer")

