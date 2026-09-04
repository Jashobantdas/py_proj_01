from pydantic import BaseModel

class DepartmentSch(BaseModel):
    id: int
    name: str

    def __repr__(self):
        return f"Department(id= {self.id}, name= {self.name})"

class EmployeeDept(BaseModel):
    id: int
    name: str
    salary: float
    d_id: int

class DepartmentSchWithEmployee(BaseModel):
    id: int
    name: str
    employees: list[EmployeeDept]
    def __repr__(self):
        return f"Department(id= {self.id}, name= {self.name})"

class CreateEmployee(BaseModel):
    name: str
    salary: float
    d_id: int

    def __repr__(self):
        return f"CreateEmployee(name= {self.name}, salary= {self.salary}, d_id= {self.d_id})"

class GetEmployee(BaseModel):
    id: int
    name: str
    salary: float
    dept: DepartmentSch

    def __repr__(self):
        return f"GetEmployee(e_id= {self.id}, name= {self.name}, salary= {self.salary}, dept= {self.dept})"

class UserSch(BaseModel):
    id: int
    first_name: str
    last_name: str
    u_name: str
    email: str
    password: str
    role: str

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, u_name={self.u_name}, email={self.email}, password={self.password}, role={self.role})"

class LonaApprovalModel(BaseModel):
    loan_id : int
    no_of_dependents : int
    education: str
    self_employed: str
    income_annum : int
    loan_amount : float | int
    loan_term : int
    cibil_score : int
    residential_assets_value : int
    commercial_assets_value : int
    luxury_assets_value : int
    bank_asset_value : int

    def __repr__(self):
        return f"LonaApprovalModel(loan_id = {self.loan_id}, loan_name = {self.loan_name}, no_of_dependents : {self.no_Of_dependent}, income_annum : {self.income_annum}, loan_amount = {self.loan_amount}, loan_term = {self.loan_term}, cibil_score = {self.cibil_score}, residential_assets_value = {self.residential_assets_value}, commercial_assets_value = {self.commercial_assets_value}, luxury_assets_value = {self.luxury_asset_value}, bank_asset_value = {self.bank_asset_value})"

class ProductSch(BaseModel):
    id : int
    title : str
    description : str
    category : str
    price : float
    discountPercentage : float
    rating : float
    stock : int
    tags : list
    brand : str
    sku : str
    weight : int
    dimensions : dict
    warrantyInformation : str
    shippingInformation : str
    availabilityStatus : str
    reviews : list
    returnPolicy : str
    minimumOrderQuantity : int
    meta : dict
    images : list
    thumbnail : str

    def __repr__(self) -> str:
        return super().__repr__()



