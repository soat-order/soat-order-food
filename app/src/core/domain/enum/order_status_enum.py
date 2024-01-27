from enum import Enum

class OrderStatusEnum(Enum):
    RECEIVED = "RECEBIDO"
    IN_PREPARATION = "EM PREPARAÇÃO"
    READY = "PRONTO"
    FINISHED = "FINALIZADO"

    @classmethod
    def valueOfValid(cls, value) -> bool:
        # return name in cls.__members__
        return any(enumType for enumType in cls if enumType.value == str(value).upper() or enumType.name == str(value).upper())

    @classmethod
    def valueOf(cls, value):
        # return name in cls.__members__
        for enumType in cls:
            if (enumType.value == str(value).upper() or enumType.name == str(value).upper()):
                return enumType
        return None
