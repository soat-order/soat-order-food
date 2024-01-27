from typing import List, Any
from src.adapter.spi.persistence.model.order_item import OrderItem as OrderItemModel
from src.core.domain.order_item import OrderItem


class OrderItemMapper:
    @staticmethod
    def parseToModel(domain: OrderItem) -> OrderItemModel:
        return OrderItemModel(productId=domain.productId, quantity=domain.quantity,
                         amount=domain.amount, note=domain.note)

    @staticmethod
    def parseToModelList(domainList: List[OrderItem]) -> List[OrderItemModel]:
        return [OrderItemMapper.parseToModel(domain) for domain in domainList]

    @staticmethod
    def parseToDomain(model: OrderItemModel) -> OrderItem:
        orderItem = OrderItem(productCode=None, quantity=model.quantity,
                         amount=model.amount, note=model.note)
        orderItem.productId = model.productId   
        orderItem.productName = None     
        return orderItem

    @staticmethod
    def parseToDomainList(modelList: List[OrderItemModel]) -> List[OrderItemModel]:
        return [OrderItemMapper.parseToDomain(model) for model in modelList]

    @staticmethod
    def parseDictToModel(dictModel) -> Any:
        # devido ao findAll retornar um CURSOR neste caso precisa chamar o metodo parseDictToModelList
        if (not isinstance(dictModel, dict)):
            return OrderItemMapper.parseDictToModelList(dictModel)
        item = OrderItemModel(productId=dictModel['productId'],quantity=dictModel['quantity'],
                               amount=dictModel['amount'],note=dictModel['note'])
        return item

    @staticmethod
    def parseDictToModelList(dictList: List[dict]) -> List[OrderItemModel]:
        return list(OrderItemMapper.parseDictToModel(dict) for dict in dictList)
