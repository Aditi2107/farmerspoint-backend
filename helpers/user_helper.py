

from typing import Optional


class UserHelper:
    def __init__(
        self,
        phonenumber: str,
        name: str,
        password_hash: str,
        role: str,
        id: Optional[int] = None
    ) -> None:
        self.id = id
        self.phonenumber = phonenumber
        self.name = name
        self.password_hash = password_hash
        self.role = role

    @staticmethod
    def from_dict(data: dict) -> "UserHelper":
        return UserHelper(
            id=data.get["id"],
            phonenumber=data["phonenumber"],
            name=data["name"],
            password_hash=data["password_hash"],
            role=data["role"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "phonenumber": self.phonenumber,
            "name": self.name,
            "password_hash": self.password_hash,
            "role": self.role,
        }
