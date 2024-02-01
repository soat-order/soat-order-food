from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.product_put_usecase import ProductPutUseCaseImpl
from src.core.domain.enum.producty_type_enum import ProductType
from src.core.domain.product import Product
from src.adapter.spi.persistence.model.product import Product as ProductModel
from src.adapter.spi.persistence.repository.product_repository import ProductRepository


class ProductPuttUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : ProductPutUseCaseImpl = ProductPutUseCaseImpl()
        self.productMock: Product = Product("1","PRODUTO TESTE", 1.0, ProductType.BEVERAGE)
        self.productModelMock: ProductModel = ProductModel("1","PRODUTO TESTE", 1.0, ProductType.BEVERAGE.name)
    
    @patch.object(ProductRepository, 'findById')
    @patch.object(ProductRepository, 'update')
    def test_execute_ok(self, mock_repository_findById, mock_repository_update):
        mock_repository_findById.return_value = self.productModelMock
        mock_repository_update.return_value = self.productMock

        result = self.useCase.execute(self.productMock)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Product)
        self.assertEqual(result.name, self.productMock.name)
