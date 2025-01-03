from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str | None = None
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(UserBase):
    email: EmailStr | None = None


class UserOut(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True
