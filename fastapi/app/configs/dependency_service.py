from repositories.department_repository import DepartmentRepository
from repositories.employee_repository import EmployeeRepository

from configs.database import get_db
from fastapi.params import Depends

from repositories.user_repository import UserRepository
from services.department_service import DepartmentService
from services.employee_service import EmployeeService
from sqlalchemy.orm import Session

from services.model_services import ModelServices
from services.product_service import ProductService
from services.rag_service import RagService
from services.user_service import UserService


def get_emp_repo(db: Session = Depends(get_db)) -> EmployeeRepository:
    return EmployeeRepository(db)

def get_emp_service(repo: EmployeeRepository = Depends(get_emp_repo)) -> EmployeeService:
    return EmployeeService(repo)

def get_dept_repo(db: Session = Depends(get_db)) -> DepartmentRepository:
    return DepartmentRepository(db)

def get_dept_service(repo: DepartmentRepository = Depends(get_dept_repo)) -> DepartmentService:
    return DepartmentService(repo)

def get_user_repo(repo: UserRepository = Depends(get_db)) -> UserRepository:
    return UserRepository(repo)

def get_user_service(repo: UserRepository = Depends(get_user_repo)) -> UserService:
    return UserService(repo)

def get_product_service():
    return ProductService()

def get_model_service():
    return ModelServices()

def get_rag_service():
    return RagService()