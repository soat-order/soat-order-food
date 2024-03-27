from enum import Enum

class Contants(Enum):
    SQS_HOST = "localhost:4576"
    SQS_HOST_QUEUE = f"{SQS_HOST}/queue"
    AWS_REGION = "sa-east-1"
    AWS_ACCESS_KEY = ""
    AWS_SECRET_KEY = ""
