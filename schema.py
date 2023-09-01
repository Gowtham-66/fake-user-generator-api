
from pydantic import BaseModel

class user(BaseModel):
    name : str
    lastname : str


class fake(BaseModel):
    name: str
    address: str
    email: str
    profile_picture: str
