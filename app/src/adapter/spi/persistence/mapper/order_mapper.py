from typing import List
from src.core.domain.order import Order
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.adapter.spi.persistence.model.order import Order as OrderModel
from src.adapter.spi.persistence.mapper.order_item_mapper import OrderItemMapper

class OrderMapper:
    @staticmethod
    def parseToModel(domain: Order) -> OrderModel:        
        model = OrderModel(
            customerName=domain.customerName,
            customerIdentify=domain.customerIdentify, 
            deliveryAmount=domain.deliveryAmount,
            totalAmount=domain.total,
            status=domain.status.value,
            items=OrderItemMapper.parseToModelList(domain.items)
        )
        if (domain.id != None):
            model.id = domain.id
        return model
    
    @staticmethod
    def parseToDomain(model: OrderModel) -> Order:
        print(model.status)
        domain = Order(
            customerName=model.customerName,
            customerIdentify=model.customerIdentify,
            status=OrderStatusEnum.valueOf(model.status),
            items=OrderItemMapper.parseToDomainList(model.items)
        )
        domain.issueDateTime = model.issueDateTime
        domain.deliveryAmount = model.deliveryAmount
        domain.total = model.totalAmount
        domain.id = model.id
        return domain

    @staticmethod
    def parseToDomainList(modelList: List[OrderModel]) -> List[Order]:
        return [OrderMapper.parseToDomain(model) for model in modelList]
            
    @staticmethod
    def parseDictToModel(dictModel) -> OrderModel:
        # devido ao findAll retornar um CURSOR neste caso precisa chamar o metodo parseDictToModelList
        if (not isinstance(dictModel, dict)):
            return OrderMapper.parseDictToModelList(dictModel)
        order = OrderModel(
            customerName=dictModel['customerName'],
            customerIdentify=dictModel['customerIdentify'],
            deliveryAmount=dictModel['deliveryAmount'],
            totalAmount=dictModel['totalAmount'],
            status=dictModel['status'],
            items=OrderItemMapper.parseDictToModelList(dictModel['items'])
        )
        order.issueDateTime = dictModel['issueDateTime']
        order.id = dictModel['_id']
        return order

    @staticmethod
    def parseDictToModelList(dictList: List[dict]) -> List[OrderModel]:
        return list(OrderMapper.parseDictToModel(dict) for dict in dictList)
