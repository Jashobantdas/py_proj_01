from typing import List

from sqlalchemy import select, func

from model.models import Employee, Department
from sqlalchemy.orm import Session, contains_eager


class EmployeeRepository:
    def __init__(self, db: Session):
        self.session = db

    def save(self, employee: Employee) -> Employee:
        self.session.add(employee)
        self.session.commit()
        return self.session.query(Employee).join(Employee.department).options(contains_eager(Employee.department)).filter(Employee.id == employee.id).populate_existing().first()

    def fetch_all(self) -> List[Employee]:
        stmt = select(Employee,Department).join(Department)
        return self.session.execute(stmt).all()

    def fetch_by_id(self,e_id)-> Employee:
        emp =  self.session.query(Employee).join(Employee.department).options(contains_eager(Employee.department)).filter(Employee.id == e_id).first()

        print(type(emp))
        print(emp.__repr__())
        return emp

    def update(self, employee_data: Employee) -> Employee:
        employee = self.session.get(Employee, employee_data.id)

        if not employee:
            raise Exception("Employee not found")

        employee.name = employee_data.name
        employee.salary = employee_data.salary
        employee.d_id = employee_data.d_id

        self.session.commit()
        self.session.refresh(employee)

        return employee_data

    def delete(self, e_id: int) -> Employee:
        employee = self.fetch_by_id(e_id)
        print(employee)
        if employee:
            self.session.delete(employee)
            self.session.commit()

    def fetch_by_department(self,d_id) -> List[Employee]:
        stmt = select(Employee,Department).join(Department).where(Employee.d_id == d_id)
        return self.session.execute(stmt).scalars().all()

    def is_present(self,e_id):
        return self.session.execute(select(func.count).select_from(Employee).where(Employee.id == e_id)).scalar() > 0
