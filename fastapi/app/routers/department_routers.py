from configs.dependency_service import get_dept_service
from fastapi import APIRouter, Depends

from schema.schemas import DepartmentSch
from services.department_service import DepartmentService

d_router = APIRouter()

@d_router.get("/details")
def get_department(service:DepartmentService=Depends(get_dept_service)):
    return service.get_department()

@d_router.get("/")
def get_department_with_employee(service:DepartmentService=Depends(get_dept_service)):
    return service.get_department_with_employee()

@d_router.get("/{id}")
def get_department_by_id(id: int, service:DepartmentService=Depends(get_dept_service)):
    return service.get_department_by_id(id)

@d_router.post("/")
def add_department(department: DepartmentSch,service:DepartmentService=Depends(get_dept_service)):
    return service.add_department(department)

@d_router.put("/")
def update_department(department: DepartmentSch,service:DepartmentService=Depends(get_dept_service)):
    return service.update_department(department)

@d_router.delete("/")
def delete_department(id: int,service:DepartmentService=Depends(get_dept_service)):
    return service.delete_department(id)