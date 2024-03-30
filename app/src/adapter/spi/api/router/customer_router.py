from fastapi import APIRouter, status, Path, Depends
from src.port.usecase.customer_post_usecase import CustomerPostUseCase
from src.port.usecase.customer_put_usecase import CustomerPutUseCase
from src.port.usecase.customer_get_usecase import CustomerGetUseCase
from src.core.domain.user_logged import UserLogged
from src.core.deps.deps import token_validade
from src.core.usecase.customer_post_usecase import CustomerPostUseCaseImpl
from src.core.usecase.customer_put_usecase import CustomerPutUseCaseImpl
from src.core.usecase.customer_get_usecase import CustomerGetUseCaseImpl
from src.adapter.spi.api.schema.customer_request import CustomerRequest
from src.adapter.spi.api.schema.customer_inactive_request import CustomerInactiveRequest
from src.adapter.spi.api.schema.customer_update_request import CustomerUpdateRequest
from src.adapter.spi.api.validator.validator import Validator
from src.adapter.spi.api.mapper.customer_mapper import CustomerMapper
from src.config.settings_config import settings

router = APIRouter()
__customerPostUseCase: CustomerPostUseCase = CustomerPostUseCaseImpl()
__customerPutUseCase: CustomerPutUseCase = CustomerPutUseCaseImpl()
__customerGetUseCase: CustomerGetUseCase = CustomerGetUseCaseImpl()

validator: Validator = Validator()

@router.post(path='/', status_code=status.HTTP_201_CREATED)
async def save(customer: CustomerRequest):
    validator.validateCustomer(customer)
    __customerPostUseCase.execute(CustomerMapper.parseToDomain(customer))    

@router.put(path='/', status_code=status.HTTP_204_NO_CONTENT)
async def update(customer: CustomerUpdateRequest):
    # validator.validateCustomer(customer)
    __customerPutUseCase.execute(CustomerMapper.parseUpdateToDomain(customer))    

@router.put(path='/{id}/inactive', status_code=status.HTTP_204_NO_CONTENT)
async def inactive(id: str, customerInactiveRequest: CustomerInactiveRequest):
    # validator.validateCustomer(customer)
    __customerPutUseCase.inactive(id=id, inactive=customerInactiveRequest.inactive)

@router.get(path='/{id}', status_code=status.HTTP_200_OK)
async def getById(id: str, userLogged : UserLogged = Depends(token_validade)):
    return CustomerMapper.parseToResponse(__customerGetUseCase.getById(id))    

@router.get(path='/document/{documentNumber}', status_code=status.HTTP_200_OK)
async def getByDocumentNumber(documentNumber: str = Path(..., title="Valid document number", regex="([0-9]{11})|([0-9]{14})"),
        userLogged : UserLogged = Depends(token_validade)):    
    return CustomerMapper.parseToResponse(__customerGetUseCase.getByDocumentNumber(documentNumber))    

@router.get(path='/', status_code=status.HTTP_200_OK)
async def getAll(userLogged : UserLogged = Depends(token_validade)):
    return CustomerMapper.parseToResponseList(__customerGetUseCase.getByAll())
