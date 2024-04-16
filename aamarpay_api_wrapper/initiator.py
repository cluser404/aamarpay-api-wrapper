from abc import ABC
import requests

from .payment import Payment
from .initiation_response import InitiationResponse
from .initiation_response_creator import InitiationResponseCreator
from .errors import InvalidSignatureKeyError
from .errors import InvalidStoreIDError


class Initiator(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    def initiate_payment(self, payment: Payment) -> InitiationResponse:
        response = requests.post(self.base_url, json=payment.to_dict())
        data = response.json()
        print(data)

        if type(data) == str:
            if data == "Invalid Signature Key":
                raise InvalidSignatureKeyError("Please provide a valid signature key")
            elif data == "Invalid Store ID":
                raise InvalidStoreIDError("Please provide a valid store id")

        payment_initiation_response = InitiationResponseCreator().create_from_dict(data)
        return payment_initiation_response
