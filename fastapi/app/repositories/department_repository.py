from typing import List

from model.models import Department, Employee
from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.orm import Session, selectinload


class DepartmentRepository:
    def __init__(self, session:Session):
        self.session = session

    def find_all(self)->List[Department]:
        return self.session.scalars(select(Department)).all()

    def find_by_id(self,d_id:int)->Department:
        return self.session.get(Department, d_id)

    def add(self,dept:Department)->Department:
        self.session.add(dept)
        self.session.commit()
        self.session.refresh(dept)
        return dept

    def update(self,dept:Department)->Department:
        cur_dept = self.session.get(Department, dept.id)
        if cur_dept is None:
            return None

        cur_dept.name = dept.name

        self.session.commit()
        self.session.refresh(cur_dept)
        return cur_dept

    def delete(self,id:int):
        result = self.session.get(Department, id)
        if result is None:
            return False
        self.session.delete(result)
        self.session.commit()
        return True

    def is_exist(self,id: int)->bool:
        stmt = (select(func.count()).select_from(Department).where(Department.id == id))
        return self.session.scalar(stmt) > 0

    def find_all_dept_with_employee(self):
        stmt = (select(Department).options(selectinload(Department.employees)))
        return self.session.execute(stmt).scalars().all()