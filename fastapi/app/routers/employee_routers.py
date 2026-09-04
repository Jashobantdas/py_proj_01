from typing import List

from configs.dependency_service import get_emp_service
from fastapi import APIRouter
from fastapi.params import Depends
from schema.schemas import GetEmployee, CreateEmployee
from services.employee_service import EmployeeService

e_router = APIRouter()

@e_router.get("/")
def get_employees(e_service:EmployeeService=Depends(get_emp_service)) -> List[GetEmployee]:
    return e_service.get_employee()

@e_router.get("/{e_id}")
def get_employee_by_id(e_id:int, e_service:EmployeeService=Depends(get_emp_service))->GetEmployee:
    return e_service.get_employee_by_id(e_id)

@e_router.post("/")
def create_employee(employee: CreateEmployee, e_service:EmployeeService=Depends(get_emp_service)) -> GetEmployee:
    print(f"from e_router: employee is {employee}")
    return e_service.insert_employee(employee)

@e_router.put("/")
def update_employee(employee: GetEmployee, e_service:EmployeeService=Depends(get_emp_service)) -> GetEmployee:
    return e_service.update_employee(employee)

@e_router.delete("/{e_id}")
def delete_employee(e_id:int,e_service:EmployeeService=Depends(get_emp_service)):
    print(e_id)
    return e_service.delete_employee(e_id)