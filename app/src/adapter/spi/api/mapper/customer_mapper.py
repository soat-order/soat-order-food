from typing import List
from src.adapter.spi.api.schema.base_response import BaseResponse
from src.adapter.spi.api.schema.customer_request import CustomerRequest
from src.adapter.spi.api.schema.customer_update_request import CustomerUpdateRequest
from src.adapter.spi.api.schema.customer_reponse import CustomerResponse
from src.core.domain.customer import Customer


class CustomerMapper:
    @staticmethod
    def parseToDomain(request: CustomerRequest) -> Customer:
        return Customer(name=request.name, documentNumber=request.documentNumber,
                                    email=request.email, phoneNumber=request.phoneNumber)

    @staticmethod
    def parseUpdateToDomain(request: CustomerUpdateRequest) -> Customer:
        customer: Customer = Customer(name=request.name, documentNumber=None,
                    email=request.email, phoneNumber=request.phoneNumber)        
        customer.id = request.id        
        return customer

    @staticmethod
    def parseToResponse(domain: Customer) -> BaseResponse[CustomerResponse]:
        return BaseResponse(data=CustomerResponse(id=domain.id, name=domain.name, documentNumber=domain.documentNumber,
                                email=domain.email,phoneNumber=domain.phoneNumber,inactive=domain.inactive))
    
    @staticmethod
    def parseToResponseList(domainList: List[Customer]) -> BaseResponse[CustomerResponse]:
        return BaseResponse(data=[CustomerMapper.parseToResponse(domain).data for domain in domainList])        
