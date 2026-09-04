from typing import List

from configs.custom_exception import NotFoundException
from model.models import Department
from repositories.department_repository import DepartmentRepository
from schema.schemas import DepartmentSch, EmployeeDept, DepartmentSchWithEmployee


class DepartmentService:
    def __init__(self, repo:DepartmentRepository):
        self.d_repo = repo

    def get_department(self) -> List[DepartmentSch]:
        dept = self.d_repo.find_all()
        if dept is None:
            raise NotFoundException("Department not found.")
        dept_list = [DepartmentSch(id=de.id,name=de.name) for de in dept]
        print(dept_list)
        return dept_list

    def get_department_by_id(self, d_id: int) -> DepartmentSch:
        dept = self.d_repo.find_by_id(d_id)
        if dept is None:
            raise NotFoundException("Department not found.")
        dept_sch = DepartmentSch(id=dept.id,name=dept.name)
        return dept_sch

    def get_department_with_employee(self) -> List[DepartmentSch]:
        dept = self.d_repo.find_all_dept_with_employee()
        print("line no=32",dept)
        if dept is None:
            raise NotFoundException("Department not found.")
        dept_list = []
        for de in dept:
            emp_list = [EmployeeDept(id=emp.id,name=emp.name,salary=emp.salary,d_id=emp.d_id) for emp in de.employees]
            dept_list.append(DepartmentSchWithEmployee(id=de.id, name=de.name,employees=emp_list))
        print(dept_list)
        return dept_list

    def add_department(self, department: DepartmentSch)->DepartmentSch:
        dept = Department(name=department.name)
        dept = self.d_repo.add(dept)
        if dept is None:
            raise NotFoundException("Department not added successfully.")
        return DepartmentSch(id=dept.id,name=dept.name)

    def update_department(self, department: DepartmentSch)->DepartmentSch:
        dept = self.d_repo.update(Department(id=department.id,name=department.name))
        if dept is None:
            raise NotFoundException("Department not updated successfully.")
        return DepartmentSch(id=dept.id,name=dept.name)

    def delete_department(self, d_id: int):
        check = False
        if self.d_repo.is_exist(d_id):
            check = self.d_repo.delete(d_id)
        else:
            raise NotFoundException("Department not found.")

        if check:
            return "Department deleted successfully."
        return "Department not deleted."