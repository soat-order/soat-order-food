from typing import List
from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.product_get_usecase import ProductGetUseCaseImpl
from src.core.domain.enum.producty_type_enum import ProductType
from src.core.domain.product import Product
from src.adapter.spi.persistence.model.product import Product as ProductModel
from src.adapter.spi.persistence.repository.product_repository import ProductRepository


class ProductGetUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : ProductGetUseCaseImpl = ProductGetUseCaseImpl()
        self.productMock: Product = Product("1","PRODUTO TESTE", 1.0, ProductType.BEVERAGE)
        self.productModelMock: ProductModel = ProductModel("1","PRODUTO TESTE", 1.0, ProductType.BEVERAGE)

    @patch.object(ProductRepository, 'findById')
    def test_findById_ok(self, mock_repository_findById):
        mock_repository_findById.return_value = self.productModelMock        
        result = self.useCase.getById("1")
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Product)
        self.assertEqual(result.code, self.productMock.code)

    @patch.object(ProductRepository, 'findByCode')
    def test_findByCode_ok(self, mock_repository_findByCode):
        mock_repository_findByCode.return_value = self.productModelMock        
        result = self.useCase.getByCode("1")
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Product)
        self.assertEqual(result.code, self.productMock.code)

    @patch.object(ProductRepository, 'findByAll')
    def test_getByAll_ok(self, mock_repository_findByAll):
        mock_repository_findByAll.return_value = [self.productModelMock]        
        result = self.useCase.getByAll()
        self.assertIsNotNone(result)
        self.assertEqual(type(result), list)
        self.assertEqual(result[0].code, self.productMock.code)


    @patch.object(ProductRepository, 'findByFilter')
    def test_getByType_ok(self, mock_repository_findByFilter):
        mock_repository_findByFilter.return_value = [self.productModelMock]
        result = self.useCase.getByType(ProductType.BEVERAGE.name)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), list)
        self.assertEqual(result[0].type, self.productMock.type)
