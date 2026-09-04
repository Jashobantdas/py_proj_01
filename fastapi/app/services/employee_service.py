from configs.custom_exception import NotFoundException, AlreadyExistsException
from model.models import Employee
from repositories.employee_repository import EmployeeRepository
from schema.schemas import CreateEmployee, GetEmployee, DepartmentSch


class EmployeeService:
    def __init__(self, repo: EmployeeRepository):
        self.e_repo = repo

    def get_employee(self):
        emp_model_list = self.e_repo.fetch_all()

        if emp_model_list is None:
            raise NotFoundException("Employee not found...")

        print(emp_model_list)

        emp_sch_list = [GetEmployee(id=emp.id, name=emp.name, salary=emp.salary, dept=DepartmentSch(id=dept.id, name=dept.name)) for emp,dept in emp_model_list]
        emp_sch_list = sorted(emp_sch_list, key=lambda emp: emp.id)
        print(emp_sch_list)
        return emp_sch_list


    def get_employee_by_id(self, e_id: int)->GetEmployee|None:
        employee = self.e_repo.fetch_by_id(e_id)

        if employee is None:
            raise NotFoundException("Employee not found...")

        emp = GetEmployee(
            id= employee.id,
            name= employee.name,
            salary= employee.salary,
            dept= DepartmentSch(
                id= employee.department.id,
                name= employee.department.name
            )
        )

        return emp

    def insert_employee(self, emp: CreateEmployee)->GetEmployee|None:
        employee = Employee()
        employee.name = emp.name
        employee.salary = emp.salary
        employee.d_id = emp.d_id

        print(f"EmployeeMoels={employee}")

        if emp is not None:
            employee = self.e_repo.save(employee)

        if employee is None:
            raise AlreadyExistsException("Employee already exists...")

        emp = GetEmployee(
            id=employee.id,
            name=employee.name,
            salary=employee.salary,
            dept=DepartmentSch(
                id=employee.department.id,
                name=employee.department.name
            )
        )
        print(f"line no 66. emp = {emp}")
        return emp

    def update_employee(self, employee: GetEmployee) -> GetEmployee|None:
        if employee is not None:
            model = Employee(id=employee.id,name=employee.name,salary=employee.salary,d_id=employee.dept.id)
            model = self.e_repo.update(model)

            employee = GetEmployee(
                id=model.id,
                name=model.name,
                salary=model.salary,
                dept=DepartmentSch(
                    id=model.d_id,
                    name=employee.dept.name
                )
            )
        else:
            return None

        return employee

    def delete_employee(self, e_id: int):
        self.e_repo.delete(e_id)

