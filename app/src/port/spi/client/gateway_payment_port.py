from abc import ABC, abstractmethod


class GatewayPaymentPort(ABC):
    @abstractmethod
    def paid(self, paymentId: str):
        return NotImplementedError
    
    @abstractmethod    
    def cancel(self, paymentId: str):
        return NotImplementedError    