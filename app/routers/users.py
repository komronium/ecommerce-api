from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserOut
from app.services.users import UserService

router = APIRouter(
    tags=['Users'],
    prefix='/api/users'
)


@router.get('/', response_model=List[UserOut], status_code=status.HTTP_200_OK)
async def get_all_user(db: Session = Depends(get_db)):
    return await UserService.get_all_users(db)

