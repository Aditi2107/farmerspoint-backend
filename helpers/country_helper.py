


from typing import Optional

class CountryHelper:
    def __init__(
        self,
        country_name: str,
        id: Optional[int] = None
    ) -> None:
        self.id = id
        self.country_name = country_name

    @staticmethod
    def from_dict(data: dict) -> "CountryHelper":
        return CountryHelper(
            id=data.get("id"),  
            country_name=data["country_name"]
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "country_name": self.country_name
        }
