from typing import Any
from src.adapter.spi.persistence.repository.repository_default import RepositoryDefault
from src.adapter.spi.persistence.model.order import Order
from src.adapter.spi.persistence.mapper.order_mapper import OrderMapper
from src.core.exception.business_exception import BusinessException


class OrderRepository(RepositoryDefault[Order, str]):
    def __init__(self) -> None:
        super().__init__(Order)

    def updateStatus(self, order: Order) -> Order:
        try:
            filter = { '_id': f"{order.id}" }
            updateStatusValue: dict = {"$set": {'status': f"{order.status}"}}
            return self._getSession().update_one(filter, updateStatusValue)
        except Exception as ex:
            raise ex


    def findByCustomerIdentify(self, customerIdentify: str) -> Order:
        try:
            return self.parseToModel(super().getDB().findByFilter(filter={"customerIdentify": customerIdentify}))
        except Exception as ex:            
            raise BusinessException(status_code=404,
                            detail=f"Not found {self.modelType.__name__} by customer :{customerIdentify}")        

    def parseToModel(self, dict: dict) -> Order:
        return OrderMapper.parseDictToModel(dict)
