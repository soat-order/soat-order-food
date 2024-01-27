from typing import Generic, TypeVar, List, Any
from src.core.util.string_util import StringUtil
from src.core.domain.enum.producty_type_enum import ProductType
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.core.exception.business_exception import BusinessException
from src.adapter.spi.api.schema.customer_request import CustomerRequest
from src.adapter.spi.api.schema.product_request import ProductRequest
from src.adapter.spi.api.schema.product_update_request import ProductUpdateRequest
from src.adapter.spi.api.schema.order_request import OrderRequest
import re

T = TypeVar("T")


#bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

UUID_REGEX = "[\w\-]{36}" 
EMAIL_REGEX = "[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}" 
AMOUNT_REGEX = "[\d]{1}||[\d]+[\.][\d]{1,2}"
PHONE_REGEX = "(^[0-9]{2}[0-9]{1}[0-9]{8}$)"
CPF_CNPJ_REGEX = "(^\d{3}\.\d{3}\.\d{3}\-\d{2}$)|(^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$)"

class Validator(Generic[T]):
    def __init__(self) -> None:
        super().__init__()
        self.error_message : List[str] = []
    
    # def __validate(self, nameField: str, typeField: T, valueField: Any) -> List[str]:
    #     if (not isinstance(valueField, typeField)):
    #         self.error_message.append("The value is invalid for field {}: {}".format(nameField, valueField))

    def __validate(self, name: str, regEx: str, value: Any) -> List[str]:
        if (value == None or not re.match(r"{}".format(regEx), value)):
            self.error_message.append("The value is invalid for field {}: {}".format(name, value))

    def __validateTrue(self, name: str, valid: bool) -> List[str]:
        if (not valid):
            self.error_message.append("The value is invalid for field {}".format(name))

    def validateCustomer(self, customer: CustomerRequest):
        self.error_message = []
        self.__validateTrue("name", customer.name != None and customer.name != "")
        self.__validate("documentNumber", CPF_CNPJ_REGEX, customer.documentNumber)
        self.__validate("email", EMAIL_REGEX, customer.email)
        self.__validate("phoneNumber", PHONE_REGEX, customer.phoneNumber)
        self.__errorHttpStatus()

    def validateProduct(self, product: ProductRequest):
        self.error_message = []
        self.__validate("code", "[A-Z0-9]{4,30}", product.code)
        self.__validate("name", "[A-Z]{4,60}", product.name)
        self.__validateTrue("amount", product.amount > 0.00)
        # self.__validate("amount", "[\d]{1}||[\d]+[\.][\d]{1,2}", str(product.amount))
        self.__validateTrue("type", ProductType.valueOfValid(product.type))
        self.__errorHttpStatus()

    def validateProductUpdate(self, productUpdate: ProductUpdateRequest):
        self.error_message = []
        self.__validate("id", UUID_REGEX, productUpdate.id)
        self.__validateTrue("amount", productUpdate.amount == None or productUpdate.amount > 0.00)
        self.__validateTrue("type", (productUpdate.type == None or ProductType.valueOfValid(productUpdate.type)))
        self.__errorHttpStatus()

    # TODO implementar validacao
    def validateOrder(self, order: OrderRequest):
        pass

    @DeprecationWarning
    def validateOrderStatus(self, status: str):
        self.error_message = []
        self.__validateTrue("status", OrderStatusEnum.valueOfValid(status))
        self.__errorHttpStatus()

    def validateEnum(self, enumType: Any, fieldName: str, fieldValue: str):
        self.error_message = []
        self.__validateTrue(fieldName, enumType.valueOf(fieldValue))
        self.__errorHttpStatus()

    def __errorHttpStatus(self, status_code: int = 400):
        if (self.error_message):
            raise BusinessException(status_code=status_code, detail={"error": self.error_message})
        

