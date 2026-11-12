
from typing import Literal
from pydantic import BaseModel, Field, field_validator


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    status: Literal["pending", "completed"] = "pending"

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("Title cannot be empty")
        return value


class TodoUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    status: Literal["pending", "completed"] = "pending"

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("Title cannot be empty")
        return value