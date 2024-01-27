import requests
from src.config.settings_config import settings
from src.port.spi.client.gateway_payment_port import GatewayPaymentPort


class PayBillClient(GatewayPaymentPort):

    def paid(self, paymentId: str):
        headers={
            'Authorization': f'Basic {settings.API_PAYBILL_TOKEN}',
            'content-type': 'application/json'
        }
        response = requests.get("{}/v1/pay/{}".format(settings.API_PAYBILL_BASE_URL, paymentId), headers=headers) 
        print(response.text)       
        if (response.status_code != 200):
            raise RuntimeError(f"Error send payment {paymentId} to gateway PayBill")

    def cancel(self, paymentId: str):
        pass
