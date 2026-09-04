from typing import List

from configs.custom_exception import NotFoundException
from model.models import User
from repositories.user_repository import UserRepository
from schema.schemas import UserSch


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_all_user(self) -> List[UserSch]|None:
        user_list = self.repo.find_all()
        print(f"UserModelList({user_list})")
        if user_list is None:
            raise NotFoundException("User not found...")
        user_sch_list = [
            UserSch(
                id=x.id,
                first_name=x.first_name,
                last_name=x.last_name,
                u_name=x.u_name,
                email=x.email,
                password=x.password,
                role=x.role
            )
            for x in user_list
        ]
        print(f"userSchemaList({user_sch_list})")
        return user_sch_list

    def get_user_by_id(self, user_id: int) -> User|None:
        user = self.repo.find_by_id(user_id)
        if user is None:
            raise NotFoundException("User not found...")
        print(f"userModel({user})")
        user_sch = UserSch(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                u_name=user.u_name,
                email=user.email,
                password=user.password,
                role=user.role
            )
        print(f"userSch({user_sch})")
        return user_sch

    def get_user_by_email(self, email: str) -> User|None:
        user = self.repo.find_by_email(email)
        if user is None:
            raise NotFoundException("User not found...")
        print(f"userModel({user})")
        user_sch = UserSch(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                u_name=user.u_name,
                email=user.email,
                password=user.password,
                role=user.role
            )
        print(f"userSch({user_sch})")
        return user_sch

