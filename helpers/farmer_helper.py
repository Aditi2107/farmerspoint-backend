

from typing import Optional


class FarmerHelper:
    def __init__(
        self,
        name: str,
        phonenumber: str,
        language: str,
        country_id: int,
        id: Optional[int] = None
    ) -> None:
        self.id = id
        self.name = name
        self.phonenumber = phonenumber
        self.language = language
        self.country_id = country_id
        

    @staticmethod
    def from_dict(data: dict) -> "FarmerHelper":
        """
        Convert dictionary data to FarmerHelper instance.
        """
        return FarmerHelper(
            id=data.get("id"),
            name=data["name"],
            phonenumber=data["phonenumber"],
            language=data["language"],
            country_id=data["country_id"],
            
        )

    def to_dict(self) -> dict:
        """
        Convert FarmerHelper instance to dictionary format.
        """
        return {
            "id": self.id,
            "name": self.name,
            "phonenumber": self.phonenumber,
            "language": self.language,
            "country_id": self.country_id
            
        }
