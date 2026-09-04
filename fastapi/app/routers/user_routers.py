from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from configs.dependency_service import get_user_service
from schema.schemas import UserSch
from services.user_service import UserService

u_router = APIRouter()

@u_router.get("/",response_model=List[UserSch])
def get_user(service: UserService = Depends(get_user_service)):
    return {
        "msg": "Successful",
        "data": service.get_all_user()
    }

@u_router.get("/{id}",response_model=UserSch)
def get_user_by_id(id:int,service: UserService = Depends(get_user_service)):
    return service.get_user_by_id(id)

@u_router.get("/{email}",response_model=UserSch)
def get_user_by_email(email: str,service: UserService = Depends(get_user_service)):
    return {
        "msg": "Successful",
        "data": service.get_user_by_email(email)
    }