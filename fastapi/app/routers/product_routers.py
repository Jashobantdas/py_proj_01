from fastapi import APIRouter, Depends

from configs.dependency_service import get_product_service
from services.product_service import ProductService

p_router = APIRouter()

@p_router.get("/")
def get_employees(p_service:ProductService=Depends(get_product_service)) :
    return p_service.get_product()

