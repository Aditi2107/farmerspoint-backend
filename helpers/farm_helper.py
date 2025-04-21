

from typing import Optional


class FarmHelper:
    def __init__(
        self,
        # country_name: str,
        area: float,
        village: str,
        crop_grown: str,
        sowing_date: str,
        country_id:int,
        farmer_id: int,
        # farmer_name: str,
        id: Optional[int] = None
    ) -> None:
        self.id = id
        # self.country_name = country_name
        self.area = area
        self.village = village
        self.country_id = country_id
        self.crop_grown = crop_grown
        self.sowing_date = sowing_date
        self.farmer_id = farmer_id
        # self.farmer_name = farmer_name

    @staticmethod
    def from_dict(data: dict) -> "FarmHelper":
        print("inside from dict")
        return FarmHelper(
            id=data.get("id"),
            # country_name=None, 
            # farmer_name=None,  # This is derived later
            country_id=data["country_id"],
            farmer_id=data["farmer_id"],
            area=data["area"],
            village=data["village"],
            crop_grown=data["crop_grown"],
            sowing_date=data["sowing_date"],
        )

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            # "country_name": self.country_name,
            "area": self.area,
            "village": self.village,
            "crop_grown": self.crop_grown,
            "sowing_date": self.sowing_date,
            "farmer_id": str(self.farmer_id),
            "country_id":self.country_id,
            # "farmer_name": self.farmer.farmer_name,
        }
