from pydantic import BaseModel
import enum
from fastapi import Query


class Role(enum.Enum):
    admin = 'admin'
    personal = 'personal'


class User(BaseModel):
    name: str
    password: str
    # ... means that the field is required, None means that it is not
    email: str = Query(..., regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
    role: Role
