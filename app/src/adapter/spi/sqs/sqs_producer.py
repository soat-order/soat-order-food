import boto3
import json
from src.core.util.logger_custom import Logger
from src.core.domain.enum.constants import Contants

class SqsProducer:
    def __init__(self) -> None:
        Logger.info(method=Logger.getMethodCurrent(), message="Start config to SQS producer")
        self.__sqs_client = boto3.client("sqs", region_name=Contants.AWS_REGION, endpoint_url=Contants.SQS_HOST) 

    def send_message(self, queue_name: str, payload: any) -> bool:
        try:        
            Logger.info(method=Logger.getMethodCurrent(), message=f"Start sending message to SQS queue: {queue_name}", data=payload)
            response = self.__sqs_client.send_message(
                QueueUrl="{}/{}".format(Contants.SQS_HOST_QUEUE, queue_name),
                MessageBody=json.dumps(payload)
            )
            Logger.info(method=Logger.getMethodCurrent(), message=f"Done sending message to SQS queue: {queue_name}", data=response)
        except Exception as ex:
            Logger.error(Logger.getClassMethodCurrent(), f"error sending message to sqs queue {queue_name} exception: {str(ex)}")
            return False;
        return True;
