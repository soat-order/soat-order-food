from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.product_post_usecase import ProductPostUseCaseImpl
from src.core.domain.enum.producty_type_enum import ProductType
from src.core.domain.product import Product
from src.adapter.spi.persistence.model.product import Product as ProductModel
from src.adapter.spi.persistence.repository.product_repository import ProductRepository


class CustomerPostUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : ProductPostUseCaseImpl = ProductPostUseCaseImpl()
        self.productMock: Product = Product("1","PRODUTO TESTE", 1.0, ProductType.BEVERAGE)
        self.productModelMock: ProductModel = ProductModel("1","PRODUTO TESTE", 1.0, ProductType.BEVERAGE)
    
    @patch.object(ProductRepository, 'save')
    def test_execute_ok(self, mock_repository):
        mock_repository.return_value = MagicMock(self.productModelMock)
        result = self.useCase.execute(self.productMock)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Product)
        self.assertEqual(result.name, self.productMock.name)
