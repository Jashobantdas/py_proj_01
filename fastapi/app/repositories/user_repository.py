from sqlalchemy import select, func, Select
from sqlalchemy.orm import Session

from model.models import User
from services.department_service import DepartmentService


class UserRepository:
    def __init__(self, session:Session):
        self.session = session

    def find_all(self):
        return self.session.scalars(Select(User)).all()

    def find_by_id(self, dept_id:int):
        return self.session.get(User,dept_id)

    def find_by_name(self, dept_name:str):
        return self.session.get(User,dept_name)

    def find_by_email(self, dept_email:str):
        return self.session.get(User,dept_email)

    def save(self,user:User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self,user:User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self,u_id):
        user=self.session.get(User,u_id)
        if user:
            return False
        self.session.delete(user)
        self.session.commit()
        return True

    def is_present(self,dept_id:int):
        return self.session.scalars(select(func.count()).select_from(User).where()) > 0