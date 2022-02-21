from pydantic import BaseModel


class User(BaseModel):
    id: int  # noqa: A003
    type: str  # noqa: A003
    login: str


class Organization(BaseModel):
    id: int  # noqa: A003
    login: str


class Repository(BaseModel):
    id: int  # noqa: A003
    name: str
    full_name: str
    fork: bool
    url: str

    owner: User
