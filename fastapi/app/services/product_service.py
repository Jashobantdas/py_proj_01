import requests

from repositories.employee_repository import EmployeeRepository
from schema.schemas import ProductSch


class ProductService :

    def get_product(self):

        productSch = []

        response = requests.get(
            'https://dummyjson.com/products'
        )

        if response.status_code == 200:
            productSch = response.json()
            print(productSch)
            return productSch
        else:
            return None