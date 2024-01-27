from typing import List, Any
from src.core.domain.user import User
from src.adapter.spi.persistence.model.user import User as UserModel

class UserMapper:
    @staticmethod
    def parseToModel(domain: User) -> UserModel:
        model = UserModel(username=domain.username, password=domain._password, email=domain.email)
        if (domain.id != None):
            model.id = domain.id
        return model

    @staticmethod
    def parseToDomain(model: UserModel) -> User:
        domain = User(id=model.id, username=model.username, email=model.email)
        domain._password = model.password
        return domain
        
    @staticmethod
    def parseToDomainList(modelList: List[UserModel]) -> List[User]:
        return [UserMapper.parseToDomain(model) for model in modelList]

    @staticmethod
    def parseDictToModel(dictModel) -> Any:
        # devido ao findAll retornar um CURSOR neste caso precisa chamar o metodo parseDictToModelList
        if (not isinstance(dictModel, dict)):
            return UserMapper.parseDictToModelList(dictModel)
        
        user = UserModel(username=dictModel['username'], password=dictModel['password'], email=dictModel['email'])        
        user.id = dictModel['_id']
        user.password = dictModel['password']
        user.inactive = dictModel['inactive']
        user.datatimeCreate = dictModel['datatimeCreate']
        return user

    @staticmethod
    def parseDictToModelList(dictList: List[dict]) -> List[UserModel]:
        return list(UserMapper.parseDictToModel(dict) for dict in dictList)
