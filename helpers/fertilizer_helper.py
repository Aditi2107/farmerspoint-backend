class FertilizerHelper:
    def __init__(self, id: int = None, fertilizer_name: str = None):
        self.id = id
        self.fertilizer_name = fertilizer_name

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            fertilizer_name=data.get("fertilizer_name")
        )

    def to_dict(self):
        return {
            "id": self.id,
            "fertilizer_name": self.fertilizer_name
        }
