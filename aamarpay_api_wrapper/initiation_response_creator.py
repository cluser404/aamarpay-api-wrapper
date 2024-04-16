from .errors import DuplicateTransactionIDError
from .initiation_response import InitiationResponse


class InitiationResponseCreator:
    def create_from_dict(self, data):

        if data.get("result") == None:
            if data.get("tran_id") == "Dublicate Transaction ID Provided By You.":
                raise DuplicateTransactionIDError("Please provide a unique transaction id")

        initiation_response = InitiationResponse(
            result = True if data["result"] == "true" else False,
            payment_url = data["payment_url"]
        )
        return initiation_response
