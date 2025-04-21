

from typing import Optional

import enum
from sqlalchemy import ARRAY, Enum


class QuantityUnitEnum(enum.Enum):
    TON = "ton"
    KILOGRAM = "kg"
    GRAM = "g"
    LITRE = "l"
    MILLILITRE = "ml"



class ScheduleHelper:
    def __init__(
        self,
        days_after_sowing: int,
        quantity: float,
        quantity_unit: QuantityUnitEnum,
        fertilizer_price: float,
        fertilizer_id: int,
        farm_id: int,
        id: Optional[int] = None
    ) -> None:
        self.id = id
        self.days_after_sowing = days_after_sowing
        self.quantity = quantity
        self.quantity_unit = quantity_unit
        self.fertilizer_price = fertilizer_price
        self.fertilizer_id = fertilizer_id
        self.farm_id = farm_id

    @staticmethod
    def from_dict(data: dict) -> "ScheduleHelper":
        return ScheduleHelper(
            id=data.get("id"),
            days_after_sowing=data["days_after_sowing"],
            quantity=data["quantity"],
            quantity_unit=data["quantity_unit"],
            fertilizer_price=data["fertilizer_price"],
            fertilizer_id=data["fertilizer_id"],
            farm_id=data["farm_id"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "days_after_sowing": self.days_after_sowing,
            "quantity": self.quantity,
            "quantity_unit": self.quantity_unit.value,
            "fertilizer_price": self.fertilizer_price,
            "fertilizer_id": self.fertilizer_id,
            "farm_id": self.farm_id,
        }


