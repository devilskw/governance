from argparse import ArgumentError


class AWSAccount:
    id: str
    name: str
    profile_prefix: str
    type: str
    def __init__(self, obj: dict) -> None:
        if obj == None:
            raise ArgumentError("Invalid argument for AWS Account")
        self.id = obj["id"] if "id" in obj else ""
        self.name = obj["name"] if "name" in obj else ""
        self.profile_prefix = obj["profile_prefix"] if "profile_prefix" in obj else ""
        self.type = obj["type"] if "type" in obj else ""