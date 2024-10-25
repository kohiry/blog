from sqlalchemy.ext.declarative import declarative_base

__all__ = [
    "BaseModel",
]

BaseModel = declarative_base()  # TODO like pydantic
