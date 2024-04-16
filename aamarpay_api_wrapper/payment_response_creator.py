from .payment_response import PaymentResponse


class PaymentResponseCreator:
    def create_from_dict(self, data):
        return PaymentResponse(**{k: PaymentResponse.__annotations__.get(k, lambda x: x)(v) for k, v in data.items()})
