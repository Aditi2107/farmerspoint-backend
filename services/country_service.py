

from repositories.country_repository import find_one_country, create_one_country
from helpers.country_helper import CountryHelper  

def get_or_create_country_service(country_name):
    try:
        country_name = str(country_name).strip().lower()
        print("country type",type(country_name))
        country = find_one_country(country_name)
        print("country",type(country))
        if country:
            return country
            #return CountryHelper(country).to_dict()  # Converting ORM object to dictionary
        # country_data = {"country_name": country_name}
        new_country = create_one_country(country_name)
        # new_country = CountryHelper.from_dict(country_name)                                                # Convert input dict to ORM object
        return new_country
        #return CountryHelper(new_country).to_dict()  # Converting ORM object to dictionary
    except Exception as e:
        print(e)
        return None  
