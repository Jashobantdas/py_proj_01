from fastapi import APIRouter
from fastapi.params import Depends

from configs.dependency_service import get_model_service
from schema.schemas import LonaApprovalModel
from services.model_services import ModelServices

m_routers = APIRouter()

@m_routers.post('/loan_approval')
def loan_approval(loan_approval_model: LonaApprovalModel, m_service: ModelServices = Depends(get_model_service)) :
    prediction = m_service.Loan_Approval(loan_approval_model)
    return prediction