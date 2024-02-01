from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.user_post_usecase import UserPostUseCase
from src.core.domain.user import User
from src.adapter.spi.persistence.model.user import User as UserModel
from src.adapter.spi.persistence.repository.user_repository import UserRepository


class UserPostUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : UserPostUseCase = UserPostUseCase()
        self.userMock: User = User(id="5c45e2f9-c048-4b79-a343-ffb2043713d0",username="TESTE", email="teste@email.com.br")
        self.userModelMock: UserModel = UserModel(username="TESTE",password="5c45e2f9-c048-4b79-a343-ffb2043713d0", email="teste@email.com.br")
    
    # @patch.object(UserRepository, 'save')
    # def test_create_ok(self, mock_repository):
    #     mock_repository.return_value = self.userMock
    #     result = self.useCase.create(self.userMock)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(type(result), User)
    #     self.assertEqual(result.username, self.userMock.username)
